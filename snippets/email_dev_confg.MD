# Configuring email for development

There are times when you do not want Django to send emails at all. 

For example, while developing a website, you probably don’t want to send out thousands of emails – but you may want to validate that emails will be sent to the right people under the right conditions, and that those emails will contain the correct content.

The easiest way to configure email for local development is to use the **console** email backend. This backend redirects all email to stdout, allowing you to inspect the content of mail.

The **file** email backend can also be useful during development – this backend dumps the contents of every SMTP connection to a file that can be inspected at your leisure.

Another approach is to use a “dumb” SMTP server that receives the emails locally and displays them to the terminal, but does not actually send anything. Python has a built-in way to accomplish this with a single command:

```ruby
python -m smtpd -n -c DebuggingServer localhost:1025
```

This command will start a simple SMTP server listening on port 1025 of localhost. This server simply prints to standard output all email headers and the email body. You then only need to set the **EMAIL_HOST** and **EMAIL_PORT** accordingly. For a more detailed discussion of SMTP server options, see the Python documentation for the **smtpd** module.

## Configuring the console email backend

To use the console email backend, set the **EMAIL_BACKEND** setting to **'django.core.mail.backends.console.EmailBackend'**. This will cause all emails to be written to the console, rather than being sent over the network.

```python
# settings.py
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
```

## Configuring the file email backend

To use the file email backend, set the **EMAIL_BACKEND** setting to **'django.core.mail.backends.filebased.EmailBackend'**. This will cause all emails to be stored in a directory on disk.

```python
# settings.py
EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
EMAIL_FILE_PATH = '/tmp/app-messages'  # change this to a proper location
```

## References

For information about unit-testing the sending of emails in your application, see the [Email services](https://docs.djangoproject.com/en/2.1/topics/testing/tools/#topics-testing-email) section of the testing documentation.

For more information about email configuration in **Django**, see the [Email](https://docs.djangoproject.com/en/2.1/topics/email/) section of the Django documentation.

https://docs.djangoproject.com/en/2.1/topics/email/#configuring-email-for-development