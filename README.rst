My script for doing a backup onto a formatted, mounted folder, on a
headless linux machine.

Current plan is to extend this to do incremental backups, so it
already generates checksums for all files backed up for future
backups to use.

Usage
=====
*./backup_full [options]* [**TARGET**] [**MACHINE ID**]

This will back up **TARGET** (a directory) to a named and dated folder
on the default mount point (the name coming from the **MACHINE ID**
specified).  The default mount point is '/mnt' (which is where I mount
my external hard discs), but this can be changed (see the
--mount-point option):

+---------------------------+---------------------------------------------+
| Options:                                                                |
+===========================+=============================================+
| --verbose, -v             | List files as they're backed up. With -vv   |
|                           | also print ssh hashes.                      |
+---------------------------+---------------------------------------------+
| --quiet, -q               | Don't even report the backup. Overrides     |
|                           | --verbose                                   |
+---------------------------+---------------------------------------------+
| --dryrun, -n              | Do a read-only run. Implies -v (unless      |
|                           | --quiet is specified)                       |
+---------------------------+---------------------------------------------+
| --mount_point MOUNT_POINT | Where the backup drive is mounted. Defaults |
|                           | to /mnt                                     |
+---------------------------+---------------------------------------------+
| --force, -f               | Demote fatal errors about bad links to      |
|                           | warnings, and continue backup.              |
+---------------------------+---------------------------------------------+

Exit codes:

If backup is successful, this tool exits with $? set to 0.  Otherwise,
something happened to interrupt the backup:

==== =====
Code Meaning
---- -----
2    Incorrect Parameters

3    Invalid paths (either target path, or backup path already exists)

4    Invalid link found in backup; the backup will be incomplete (to a
     greater or lesser extent depending on whether --force was specified)

5    Dependency failure; either readlink or sha256sum weren't found, or
     returned nonsense.
==== =====

If the tool does find an invalid link (one that points outside of the
backup target), it will abort the backup unless --force is specified.
If it's not forced, the backup will be truncated from that first
error, and for the time being it's up to you to tidy up after you've
fixed the link.  If force is specified it'll be a complete backup,
apart from the bad links which will be omitted.
