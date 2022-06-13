#include <python.h>
#include <string.h>

static PyObject* returnString(PyObject* self) {
	char* str = "End of the list.";
	
	return Py_BuildValue("s", str);
}

static PyMethodDef SpamMethods[] = {
	{"endOfList", returnString, METH_VARARGS, "return str."},
	{NULL, NULL, 0, NULL}
};

static PyModuleDef spammodule = { 
	PyModuleDef_HEAD_INIT, 
	"cstr", 
	"return string", 
	-1, SpamMethods
};

PyMODINIT_FUNC PyInit_cstr(void) {
	return PyModule_Create(&spammodule);
}
