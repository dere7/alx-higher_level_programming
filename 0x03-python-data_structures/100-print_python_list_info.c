#include "Python.h"

/**
 * print_python_list_info - prints some basic info about python lists
 * @p: PyObject
 */
void print_python_list_info(PyObject *p)
{
	size_t len = PyList_Size(p), i;
	PyObject *item;
	PyListObject *list = (PyListObject *)p;

	printf("[*] Size of the Python List = %ld\n", len);
	printf("[*] Allocated = %ld\n", list->allocated);

	for (i = 0; i < len; i++)
	{
		item = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, item->ob_type->tp_name);
	}
}
