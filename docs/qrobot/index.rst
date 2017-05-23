Deployment
----------

Create a new non-privileged user "qrobot":

::

    # adduser qrobot --gecos ""

Relogin as the newly created user and navigate to it's home directory.
Clone this repository into "repo" folder:

::

    $ git clone https://github.com/strands-project/qrobot repo

Navigate to the "repo" folder:

::

    $ cd repo

Run production bootstrap and update scripts as root (note that since the
"qrobot" user is not in sudoes, you need to ``su`` as the admin user
first):

::

    $ su %username%
    # ./scripts/bootstrap.sh production
    # ./scripts/update.sh

Configuration
~~~~~~~~~~~~~

Several configuration variables of the backend server are exposed in the
"config/flask.py" file. After making changes you need to restart the
application server:

::

    # supervisorctl restart qrobot

Updates
~~~~~~~

To update to the latest version run the update script as root from the
"repo" folder:

::

    # ./scripts/update.sh



Original page: https://github.com/strands-project/qrobot/blob/master/README.md