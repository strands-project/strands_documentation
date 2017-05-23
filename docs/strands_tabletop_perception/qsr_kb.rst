QSR KB and Visualisation
========================

Knowledge representation of and reasoning about QSRs using SWI-Prolog.
Specialized predicades can be used to visualize QSRs in RVIZ.

Starting the KB service
-----------------------

First the knowledge base service has to be started:

::

    roslaunch qsr_kb kb_bringup.launch

(Please note that SWI-Prolog needs to be installed; on Ubuntu run:
``sudo apt-get install swi-prolog``)

The knowledge base service provides a simple *tell and ask* interface to
a Prolog engine. Queries and answers are exchanged using strings.

Adding knowledge about QSRs to the KB
-------------------------------------

New perception events with different classifications can be added using
the *create\_event(Evt,QSRs,Loc,Classifications,Poses)* predicate, where
*Evt* denotes the event that will be generated, *QSRs* denotes a list of
QSRs between segmented object clusters, *Loc* denotes a location where
the event occured, *Classifications* denotes a list of different
classifiaction results (incl. probabilities) for all segemented object
clusters, and *Poses* denotes a list of object poses.

::

    create_event(EVT,
                 % QSRs, (Note: object names such as 'keyboard' are only used for a better understanding, there is no meaning attached to them)  
                 [['left-of', 'keyboard', 'cup'], ['left-of', 'monitor', 'cup'],
                  ['behind', 'keyboard', 'cup'], ['in-front-of', 'monitor', 'cup'],
                  ['in-front-of', 'keyboard', 'monitor'], ['right-of', 'cup', 'monitor']],
                 % Loc
                 'table27',
                 % Classifications (here bottom-up [BU], and top-down [TD])
                 [['BU', [['keyboard', 'Keyboard', 0.8], ['keyboard', 'Monitor', 0.2], 
                          ['cup', 'Cup', 0.4], ['cup', 'Mouse', 0.5], ['cup', 'Keyboard', 0.1], 
                          ['monitor', 'Keyboard', 0.1], ['monitor', 'Monitor', 0.9], 
                          ['mouse', 'Cup', 0.9], ['mouse', 'Mouse', 0.1]]], 
                  ['TD', [['keyboard', 'Keyboard', 0.9], ['keyboard', 'Monitor', 0.1], 
                          ['cup', 'Cup', 0.6], ['cup', 'Mouse', 0.2], ['cup', 'Keyboard', 0.2], 
                          ['monitor', 'Keyboard', 0.1], ['monitor', 'Monitor', 0.9], 
                          ['mouse', 'Cup', 0.1], ['mouse', 'Mouse', 0.9]]]],
                 % Poses         
                 [ ['monitor', [[1.0,0.0,0.0],[1,0,0,0]]], 
                   ['cup', [[0.5,1.0,0.0],[1,0,0,0]]], 
                   ['mouse', [[0.5,-0.5,0.0],[1,0,0,0]]],
                   ['keyboard', [[0.0,0.0,0.0],[1,0,0,0]]] ]).

Querying QSRs from the KB and visualise the result
--------------------------------------------------

QSRs can be queried using predicates such as *qsr(Rel, Obj1, Obj2, QSR)*
and *qsrT(Rel, Cls1, Cls2, QSR)* which use segmented object clusters and
object classes (or types) to retrieve QSRs repectively. For more options
please refer to the source code in
`qsr.pl <https://github.com/strands-project/strands_tabletop_perception/blob/hydro-devel/qsr_kb/src/qsr.pl>`__.

QSRs cannot directly be visualized. Using the *vis(QSRLst)* predicate
where *QSRLst* denotes a list of QSRs they can be *cached for
visualisation*. To visualise the different QSRs, one has to iterate over
the set of solutions via the *next\_vis(X)* predicate (see below).

::

    qsrT(Rel,Cls1,Cls2,QSR), vis([QSR]).

To visualize the next solution use the following predicate:

::

    next_vis(X).

If there is no more solution the predicate will return an empty list and
clear the visualization in RVIZ.

The list of *cached* QSRs can be cleared using the predicate *new\_vis*.


Original page: https://github.com/strands-project/strands_tabletop_perception/blob/hydro-devel/qsr_kb/README.md