%global           pypi_name cppy
%define debug_package %nil

Name:             python-cppy
Version:          1.3.1
Release:          1

Summary:          A Cassowary constraint solving algorithm
License:          BSD
Group:            Development/Python

URL:              https://pypi.org/project/cppy/
Source0:	https://files.pythonhosted.org/packages/source/c/cppy/%{pypi_name}-%{version}.tar.gz
BuildSystem:	python
BuildRequires:	pkgconfig(python3)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(setuptools-scm)

%description
A small C++ header library which makes it easier to write Python
extension modules.
The primary feature is a PyObject smart pointer which automatically
handles reference counting and provides convenience methods for
performing common object operations.

%files
%doc README.rst
%{python_sitelib}/%{pypi_name}
%{python_sitelib}/%{pypi_name}-%{version}.dist-info
