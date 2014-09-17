%define fname	mwaw
%define api	0.3
%define major	3
%define libname	%mklibname %{fname} %{api} %{major}
%define devname	%mklibname -d %{fname}

Summary:	Import library for some old mac text documents
Name:		libmwaw
Version:	0.3.2
Release:	1
Group:		System/Libraries
# The entire source code is LGPLv2+/MPLv2.0 except
# src/lib/MWAWOLEStream.[ch]xx which are BSD. There is also
# src/tools/zip/zip.cpp which is GPLv2+, but we do not build the binary
# it is used for.
License:	(LGPLv2+ or MPLv2.0) and BSD
Url:		http://sourceforge.net/projects/libmwaw/
Source0:	http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.xz
BuildRequires:	doxygen
BuildRequires:	boost-devel
BuildRequires:	pkgconfig(librevenge-0.0)
BuildRequires:	pkgconfig(zlib)

%description
libmwaw contains some import filters for old mac text documents
(MacWrite, ClarisWorks, ... ) based on top of the libwpd (which is
already used in three word processors). 

%package tools
Summary:	Tools to transform the supported formats into other formats
Group:		Office
License:	LGPLv2+

%description tools
Tools to transform the supported document formats into other formats.
Supported output formats are XHTML, text and raw.

%package -n %{libname}
Summary:	Import library for some old mac text documents
Group:		System/Libraries

%description -n %{libname}
Ths package contains libraries and header files for
developing applications that use %{name}.

%package -n %{devname}
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}

%description -n %{devname}
This package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q

%build
CFLAGS="%{optflags} -Qunused-arguments" \
CXXFLAGS="%{optflags} -Qunused-arguments" \
%configure \
	--disable-zip
%make

%install
%makeinstall_std
# it seems this tool is only useful on MacOS
rm -f %{buildroot}/%{_bindir}/mwawFile

%files tools
%{_bindir}/mwaw2csv
%{_bindir}/mwaw2html
%{_bindir}/mwaw2raw
%{_bindir}/mwaw2svg
%{_bindir}/mwaw2text

%files -n %{libname}
%{_libdir}/%{name}-%{api}.so.%{major}*

%files -n %{devname}
%doc CHANGES COPYING.* README
%{_includedir}/%{name}-%{api}
%{_libdir}/%{name}-%{api}.so
%{_libdir}/pkgconfig/%{name}-%{api}.pc
%doc %{_docdir}/%{name}
