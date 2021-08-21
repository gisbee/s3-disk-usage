import argparse
from os import getenv

from s3fs.core import S3FileSystem


def _parse_arguments():
    """
    Fetch command line arguments
    :return: Parsed command line arguments
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("-b", "--bucket", help="Name of the S3 bucket")
    parser.add_argument("--access-key", help="AWS access key ID")
    parser.add_argument("--secret-key", help="AWS secret access key")
    parser.add_argument(
        "-p",
        "--prefix",
        default="",
        help="Path prefix to filter results. Analogous to root directory in file storage.",
    )
    parser.add_argument(
        "-md",
        "--max-depth",
        default=3,
        help="Maximum number of directories to loop through under the root directory.",
    )
    parser.add_argument(
        "-hr",
        "--human-readable",
        help="Print size in human-readable format",
        action="store_true",
    )

    return parser.parse_args()


def _human_readable_size(size: int) -> str:
    """
    Convert bytes to more readable formats.
    :param size: size in bytes
    :return: size in Kilo/Mega/Giga bytes with units
    """
    power = 2 ** 10
    n = 0
    power_labels = {0: "", 1: "KB", 2: "MB", 3: "GB", 4: "TB"}

    while size > power:
        size /= power
        n += 1

    return f"{round(size, 2)} {power_labels[n]}"


def _init_s3fs(args):
    """
    Initialize s3fs by fetching AWS credentials
    :param args: command line arguments
    :return: s3fs object
    """
    access_key = (
        args.access_key if args.access_key else getenv("AWS_ACCESS_KEY_ID")
    )
    secret_key = (
        args.secret_key if args.secret_key else getenv("AWS_SECRET_ACCESS_KEY")
    )

    if not access_key or not secret_key:
        return S3FileSystem(anon=False)

    return S3FileSystem(
        key=access_key,
        secret=secret_key,
    )


def list_folder_sizes(root: str, max_depth: int) -> None:
    """
    List all files/folders and their size under a given S3 path
    :param root: S3 path prefix to start listing from
    :param max_depth: maximum folder depth to loop through
    :return: None
    """
    if max_depth == 0:
        return

    root_items = s3.ls(root)

    for item in root_items:
        item_size = s3.du(item)
        if args.human_readable:
            item_size = _human_readable_size(item_size)

        print(f"{item} \t\t\t\t {item_size}")

        node_items = s3.ls(item)

        if len(node_items) > 1:
            list_folder_sizes(
                root=item,
                max_depth=max_depth - 1,
            )


if __name__ == "__main__":
    args = _parse_arguments()
    s3 = _init_s3fs(args=args)

    list_folder_sizes(
        root=f"{args.bucket}/{args.prefix}",
        max_depth=int(args.max_depth),
    )
