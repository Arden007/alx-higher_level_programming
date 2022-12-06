#include <Python.h>
#include <object.h>
#include <listobject.h>

/**
 * print_python_list_info - Prints information about python objects
 * @p: PyObject pointer to print info about
 * Compile with:
 * gcc -Wall -Werror -Wextra -pedantic -std=c99 -shared
 (* -Wl,-soname,PyList -o libPyList.so -fPIC -I/usr/include/python3.4
 (* 100-print_python_list_info.c
 **/

void print_python_list_info(PyObject *p)
{
    long int size = PyList_Size(p);
    int i;
    PyListObject *obj = (PyListObject *)p;

    printf("[*] Size of the Python List = %li\n", size);
    printf("[*] Allocated = %li\n", obj->allocated);
    for (i = 0; i < size; i++)
        printf("Element %i: %s\n", i, Py_TYPE(obj->ob_item[i])->tp_name);
}
