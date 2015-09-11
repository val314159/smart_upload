# smart_upload
smartly upload your files to S3 for a public website (using smart_open)

Usage:

  smart_upload <srcdir> <destdir>

### Example 

```sh
APP_KEY=my_key
APP_SECRET=my_secret
smart_upload ./html s://$APP_KEY:$APP_SECRET@mybucket.amazon.com

```
