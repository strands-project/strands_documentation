Overview
========

This package provides a web server for serving media files (photos,
music, videos) to robot applications. The content is uploaded and
managed through a web interface, and is stored in the mongodb database
using GridFS.

Running
=======

``rosrun mongodb_media_server server.py``

Editing the available content
=============================

Goto to ``http://localhost:8027``

The 'File Manager' tab allows you to upload files of any type. The 'BLAH
Sets' tabs allow you to edit the data groupings. For example, the 'Photo
Sets' can be though of a albums of images to be shown together, likewise
with Music and Video.

Accessing the content
=====================

Every file is accessible through:

``http://localhost:8027/get_media/MEDIAKEY``

where MEDIAKEY is the id of the file, or

``http://localhost:8027/get_media_by_name/name``

where name is the filename of the media file.

The IDs of the files are retrievable via the Python api. For example, to
retrieve the items in a photo album called 'AAF-Deploy-InfoTerm':

::

    from mongodb_media_server import MediaClient

    mc = MediaClient('localhost', 62345) # or rospy.get_param('db_host') etc
    file_set = mc.get_set("Photo/AAF-Deploy-InfoTerm")
    for f in file_set:
        print "Media name:", i[0]
        print "Media type:", i[1]
        print "Media key:", i[2]
        print "Media URL: http://localhost:8027/get_media/"+i[2]

In this way it is straight forward to include managed media in a web.py
application .

Alternatively, the file can also be read in python rather than through
the web server interface.

Please see ``src/mongodb_media_server/media_client.py`` for the API.

To Do
=====

A more complete API for both the web interface (to provide file sets to
webpages not working on web.py), and for the python API (to provide file
set creation etc.)
