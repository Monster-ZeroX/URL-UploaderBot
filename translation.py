class Translation(object):

    START_TEXT = """Hello,

This is a Telegram Zoom Recoding Uploader Bot!

<b> Send me any Zoom Recoding URL link, I can upload Zoom Recoding links to telegram as File/Video </b>

Also I can set custom captions too

⭕️ Press /help for detailed instructions..."""

    HELP_USER = """Hai I'am a URL Uploader bot..
    
1. Send url (Link | New Name with Extension).
2. Send Custom Thumbnail (Optional).
3. Select the button.
   SVideo - Give File as video with Screenshots
   DFile  - Give File with Screenshots
   Video  - Give File as video without Screenshots
   DFile  - Give File without Screenshots
"""

    FORMAT_SELECTION = """Select the desired format: <a href='{}'>file size might be approximate</a>
    
Send your custum thumbnail if required.
You can use /deletethumbnail to delete the auto-generated thumbnail."""
    
    SET_CUSTOM_USERNAME_PASSWORD = """If you want to download premium videos, provide in the following format:
URL | newfilename | username | password"""


    UPGRADE_TEXT = "<b>Already Premium User✋</a>"
    
    DOWNLOAD_START = "Trying to download your file...⌛️"
    
    UPLOAD_START = "Uploading to Telegram now 📥..."
    
    AFTER_SUCCESSFUL_UPLOAD_MSG_WITH_TS = "Downloaded in {} seconds.🚀\n\nUploaded in {} seconds.✅"

    RCHD_TG_API_LIMIT = "Downloaded in {} seconds.🚀\nDetected File Size📥: {}\nSorry🥺. But, I cannot upload files greater than 1.95GB due to Telegram API limitations.😖"

    SAVED_CUSTOM_THUMB_NAIL = "Custom thumbnail saved.🌚 This will be permanent.\n\nUse /deletethumbnail to clear it.😇"

    DEL_ETED_CUSTOM_THUMB_NAIL = "Custom thumbnail cleared succesfully.🌝"

    CUSTOM_CAPTION_UL_FILE = ""

    SLOW_URL_DECED = "Gosh that seems to be a very slow URL. Since you were screwing my home, I am in no mood to download this file."

    NO_VOID_FORMAT_FOUND = "ERROR...\n<b>YouTubeDL</b> said: {}"
    
    SHOW_THUMB = "Use /deletethumbnail to clear this thumbnail."
    
    NO_THUMB = "No saved thumbnails Found!!📸\n\nSend an image to save it as your thumbnail permanently."    
