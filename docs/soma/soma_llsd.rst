SOMA Low-Level Sensory Datastore
================================

This package provides a totally optional set of helper tools for the
task of composing SOMA objects from individual observations of
real-world objects. The tools here, provide a custom set of ROS messages
and services. The classic use-case for this package being that of
collecting multiple observations of a single or multiple objects before
merging them into combined object models. In this use-case, the raw data
and low-level segmented observations are stored in the data structures
provided by this package, and are used as the source material to create
high-level SOMA objects. However, the implementation of how these things
are achieved -- data collection, segmentation, processing -- are all
left up to the application developer.

Messages
========

The messages are organised in a graph structure. The conceptual root
node is the Scene message, which contains various forms of unprocessed
robot perception data -- RGB-D data, odometry, arbitrary metadata etc.
-- that a system may use in further processing. This represents the raw
sensor output of a Robot performing some task such as taking multiple
views of a surface, whereby each view would be represented as a Scene
message. Multiple Scenes can be grouped together by sharing a common
episode\_id.

Given a ``Scene``, processing such as segmentation is usually applied to
extract objects. Each of these objects can be represented using the
``Segment`` message. There may be multiple ``Segments`` in a single
``Scene``, and the same ``Segment`` representing the same object may be
observed in multiple ``Scenes`` during a given episode. The message
types support this sort of relationship. For each segment, any number of
``Observations`` can be attached to a ``Segment``. An ``Observation``
represents the data produced by any processing performed on the
``Scene``, and is intended to store things like cropped images and
masked point clouds that describe specific observations of objects, and
the ``Segment`` links these observations together to the same object
across multiple views.

Services
========

There are multiple services designed to make it easy to insert and
extract data from the database. These are generally straightforward in
use, and there are examples in the /tests/ folder you can try out. The
only service that may bear further explanation is ``InsertSceneAuto``,
which allows you to specify robot\_pose and camera\_info topics, and
will automatically record and insert these along with ~2 seconds of
output from the /tf topic to your Scene message. Recording a brief burst
of /tf allows you to re-use it later and re-calculate things like frame
transforms. Transforming to and from a tf transformer is very easy, see
the TransformationStore class in server.py for examples. This is the
recommended way of putting scenes into the database, as it requires the
least amount of effort on the part of the user.

In general, all fields in all messages are optional, and arbitrary extra
relationships between messages can be encoded by using the meta\_data
fields, which are intended to be filled by JSON objects.

Services are deliberately kept bare-bones, as in contrast to the main
SOMA services that provide feature-rich query services, it is intended
that users of the LLSD perform more complicated query tasks by using
MongoDB queries.


Original page: https://github.com/strands-project/soma/blob/indigo-devel/soma_llsd/README.md