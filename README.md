# S3 Storage Usage

Summarize disk usage of the files with a given prefix on AWS S3. This is similar to doing `du -h` on a Linux machine.

Usage: s3du.py [-h] [-b BUCKET] [--access-key ACCESS_KEY]
               [--secret-key SECRET_KEY] [-p PREFIX] [-md MAX_DEPTH] [-hr]

Mandatory arguments:
```
  -b  | --bucket VALUE             Name of the S3 bucket
```

Optional arguments:
```
  -h  | --help                     Show this help message and exit
  -b  | --bucket BUCKET            Name of the S3 bucket
        --access-key ACCESS_KEY    AWS access key ID
        --secret-key SECRET_KEY    AWS secret access key
  -p  | --prefix PREFIX            Path prefix to filter results. Analogous to root
                                   directory in file storage.
  -md | --max-depth MAX_DEPTH      Maximum number of directories to loop through under
                                   the root directory.
  -hr | --human-readable           Print size in human-readable format
```

If arguments `access_key` and `secret_key` are not passed, values are fetched from environment variables `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY`.

## Dependencies
This script depends on package `s3fs`. Please install `s3fs` using the command
```bash
$ pip install s3fs
```
Refer to https://pypi.org/project/s3fs/ for more information on `s3fs`.
