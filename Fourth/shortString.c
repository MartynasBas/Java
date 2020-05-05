#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <Python.h>

// char *shortString(char* data);
// int main()
// {
//     char test[50] = "aaaaaaabbdddbbbeee";
//     printf("%s", shortString(test));

//     return 0;
// }



char *shortString(char* data){
    size_t len = strlen(data);
	char *result = malloc(len);
	char temp[1] = "";
	if(len<1)
		return result;
	int count=1;
	for(int index = 0; index < len-1; index++){
		if(data[index] != data[index+1]){
		  sprintf(temp, "%d", count);
		  strncat(result, &temp[0], 1);
			strncat(result, &data[index], 1);
			count=1;
		}
		else count++;
		}
    sprintf(temp, "%d", count);
    strncat(result, &temp[0], 1);
    strncat(result, &data[len-1], 1);
	return result;
}

static PyObject* shortStringError;

static PyObject* py_shortString(PyObject* self, PyObject* args) {
  char *n;
  if (!PyArg_ParseTuple(args, "s", &n)) {
      PyErr_SetString(shortStringError, "Something is wrong with given input");
      return NULL;
  }
  // int returnValue = shortString(n);
  // if (returnValue == -1) {
  //   PyErr_SetString(PyExc_ValueError, "Wrong number format");
  //   return NULL;
  // }

  return Py_BuildValue("s", shortString(n));
}

static PyMethodDef shortStringModuleMethods[] = {
  {"shortString", py_shortString, METH_VARARGS, "Replaces input string with one symbol and a number of its occurrences"},
  {NULL, NULL, 0, NULL}
};

static struct PyModuleDef shortStringModule = {
  PyModuleDef_HEAD_INIT,
  "ShortStringModule",
  "Replaces input string with one symbol and a number of its occurrences",
  -1,
  shortStringModuleMethods
};

PyMODINIT_FUNC PyInit_shortString(void)
{
  //return PyModule_Create(&shortStringModule);
  PyObject *mod =  PyModule_Create(&shortStringModule);
  shortStringError = PyErr_NewException("ShortStringModule.error", NULL, NULL);
  Py_INCREF(shortStringError);
  PyModule_AddObject(mod, "error", shortStringError);
  return mod;
}