#include <Python.h>
#include "structmember.h"

typedef struct{
  PyObject_HEAD
  float radius;
} Volume;

static void Volume_dealloc(Volume* self){
    Py_TYPE(self)->tp_free((PyObject*)self);
}

static PyObject * Volume_new(PyTypeObject *type, PyObject *args, PyObject *kwds)
{
    Volume *self;

    self = (Volume *)type->tp_alloc(type, 0);
    if (self != NULL) {
        self->radius = 0;
    }

    return (PyObject *)self;
}

static int Volume_init(Volume *self, PyObject *args, PyObject *kwds)
{
    if (! PyArg_ParseTuple(args, "f", &self->radius))
        return -1;
    return 0;
}

static PyMemberDef Volume_members[] = {
    {"radius", T_INT, offsetof(Volume, radius), 0, "sphere radius"},
    {NULL}  
};


static PyObject * Volume_getVolume(Volume* self)
{
    return Py_BuildValue("f", 4/3 * 3.14159265358979323846*(pow(self->radius, 3)));
}
static PyMethodDef Volume_methods[] = {
    {"getVolume", (PyCFunction)Volume_getVolume, METH_NOARGS, "Returns sphere volume"},
    {NULL}  
};

static PyObject* Volume_str(Volume* self){
    return PyUnicode_FromFormat("(%f)", self->radius);
}


static PyTypeObject volumeType ={
  PyVarObject_HEAD_INIT(NULL, 0) 
  "Volumes.Volume", /*tp_name*/
  sizeof(Volume), /*tp_basicsize*/
  0, /*tp_itemsize*/
  (destructor) Volume_dealloc, /*tp_dealloc*/
  0, /*tp_print*/
  0, /*tp_getattr*/
  0, /*tp_setattr*/
  0, /*tp_reserved*/
  0, /*tp_repr*/
  0, /*tp_as_number*/
  0, /*tp_as_sequence*/
  0, /*tp_as_mapping*/
  0, /*tp_hash */
  0, /*tp_call*/
  (reprfunc) Volume_str, /*tp_str*/
  0, /*tp_getattro*/
  0, /*tp_setattro*/
  0, /*tp_as_buffer*/ 
  Py_TPFLAGS_DEFAULT | Py_TPFLAGS_BASETYPE, /*tp_flags*/ 
  "Spheres volume: consists of 1 float value radius", /* tp_doc */
  0,
  0,
  0,
  0,
  0,
  0,
  Volume_methods,
  Volume_members,
  0,
  0,
  0,
  0,
  0,
  0,
  (initproc)Volume_init,
  0,
  Volume_new,
};




static struct PyModuleDef Volumes ={
  PyModuleDef_HEAD_INIT, 
  "Volumes", // name of module 
  "Contains 1 class: Volume", // module documentation, may be NULL
  -1, // size of per- interpreter state of the module, or -1 if the module keeps state in global variables. 
  NULL, NULL, NULL, NULL, NULL
};

PyMODINIT_FUNC PyInit_Volumes (void){
  PyObject* m;
  if (PyType_Ready(&volumeType)< 0) 
    return NULL;
  m = PyModule_Create(&Volumes);
  if (m == NULL)
    return NULL;
  Py_INCREF(&volumeType);
  PyModule_AddObject(m, "Volume", (PyObject*)&volumeType);
  return m; 
}