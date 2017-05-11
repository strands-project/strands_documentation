Topological maps are stored in the ``topological_maps`` collection in
the ``message_store`` database. Using
`Robomongo <http://robomongo.org/>`__ (or the ``mongodb`` tool) one can
easily run mongodb queries and updates to inspect or modify the
topological maps. See
http://docs.mongodb.org/manual/reference/method/db.collection.update/#db.collection.update
for more information about ´update´.

Robomongo
=========

To run queries in robomongo connect to the ``mongodb_store`` database
(usually running on port 62345), and then open a shell in the
``message_store`` database by right clicking on it.

Searching for Tags
==================

::

    db.getCollection('topological_maps').find(
        {pointset:'aaf_predep', '_meta.tag':'no_go'}
    )

Changing Actions of Edges
=========================

This will find all entries of pointset ``aaf_predep`` where the action
is defined as ``move_base``. Then it will set *the first* matching entry
in the ``edges`` array to ``human_aware_navigation``.

Note that this always only replaces the *first* matching value in the
array, hence this needs to be executed repeatedly until no more changes
occur. Mongodb unfortunately doesn't all yet to change all at once (see
https://jira.mongodb.org/browse/SERVER-1243)

::

    db.topological_maps.update(
        {pointset:'aaf_predep', 'edges.action':'move_base'},
        {$set: {'edges.$.action':'human_aware_navigation'}},
        {multi:true}
    )

