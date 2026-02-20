%define		packname	limmaGUI

Summary:	GUI for R-limma
Name:		R-%{packname}
Version:	1.38.0
Release:	2
License:	LGPL
Group:		X11/Applications
Source0:	http://www.bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
# Source0-md5:	50630ab8cfe8a8e8e4a273e85a53be24
URL:		http://www.bioconductor.org/packages/release/bioc/html/limmaGUI.html
BuildRequires:	R
BuildRequires:	R-limma
BuildRequires:	texlive-latex
BuildRequires:	tcl-devel
BuildRequires:	tk-devel
Requires:	R
Requires:	R-limma
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A Graphical User Interface for the limma Microarray package.

%prep
%setup -c -q -n %{packname}

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/R/library
%{_bindir}/R CMD INSTALL %{packname} -l $RPM_BUILD_ROOT%{_libdir}/R/library
# Clean up in advance of check
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -rf $RPM_BUILD_ROOT%{_libdir}/R/library/R.css

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{_libdir}/R/library/%{packname}/
%doc %{_libdir}/R/library/%{packname}/doc/
%doc %{_libdir}/R/library/%{packname}/html/
%doc %{_libdir}/R/library/%{packname}/DESCRIPTION
%{_libdir}/R/library/%{packname}/CITATION
%{_libdir}/R/library/%{packname}/NAMESPACE
%{_libdir}/R/library/%{packname}/INDEX
%{_libdir}/R/library/%{packname}/Meta/
%{_libdir}/R/library/%{packname}/R/
%{_libdir}/R/library/%{packname}/help/
%{_libdir}/R/library/%{packname}/etc/
