# S3 Storage Usage

Summarize disk usage of the files with a given prefix on AWS S3. This is similar to doing `du -h` on a Linux machine.

Usage: `python s3du.py [OPTION] prefix`

Mandatory arguments:
```
--bucket            Name of the S3 bucket
```

Optional arguments:
```
--access-key        AWS access key ID
--secret-key        AWS secret access key
--prefix            Path prefix to filter results.
                    Analogous to root directory in file storage
--max-depth         Maximum number of directories to loop through
                    under the root directory
--human-readable    Print file sizes in human readable format
```
If arguments `access_key` and `secret_key` are not passed, values are fetched from environment variables `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY`.

## Dependencies
This script depends on package `s3fs`. Please install `s3fs` using the command
```bash
$ pip install s3fs
```
Refer to https://pypi.org/project/s3fs/ for more information on `s3fs`.
