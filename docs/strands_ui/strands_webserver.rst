The STRANDS webserver package
=============================

**Quite a lot information is missing here...**

Modal Dialog
------------

The webserver offers and ``actionlib`` server to display a modal dialog.
Here is an example goal definition, the action interface is
``strands_webserver/modal_dlg``:

::

    title: 'This is a test'
    text: 'We can use full HTML in here, e.g. <b>BOLD</b>'
    buttons: ['OK', 'cancel']
    buttons_class: ['btn-success']

``buttons_class`` can be used to set `Bootstrap button
classes <http://getbootstrap.com/css/#buttons-options>`__

The full action is defined as ``ModalDialogSrv.action``:

::

    # the title of the dialog (can be full HTML)
    string title
    # the main body of the dialog (HTML)
    string text
    # the HTML definition for the individual buttons (usually just a text)
    string[] buttons
    # option bootstrap button class, e.g. 'btn-default' or 'btn-success'
    string[] buttons_class
    ---
    # returns the HTML definition of the selected button
    string button
    # returns the index of the selected button
    uint32 button_id
    ---
    string feedback

The dialog is displayed as a bootstrap modal dialog, overlaying any
information currently displayed. Preempting the actionlib goal will hide
the dialog, otherwise it is dismissed as soon as the user clicks on of
the defined buttons and the actions returns success in this case. The
action server returns "feedback" once the dialog has been rendered on
the user's screen. The feedback is the full generated HTML definition of
the dialog displayed (not very useful, but hey, at least you know when
it is displayed).


Original page: https://github.com/strands-project/strands_ui/blob/hydro-devel/strands_webserver/README.md