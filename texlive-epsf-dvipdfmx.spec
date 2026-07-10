%global tl_name epsf-dvipdfmx
%global tl_revision 35575

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2014
Release:	%{tl_revision}.1
Summary:	Plain TeX file for using epsf.tex with (x)dvipdfmx
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/plain/contrib/epsf-dvipdfmx
License:	pd
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/epsf-dvipdfmx.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/epsf-dvipdfmx.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
epsf-dvipdfmx.tex is a plain TeX file to be \input after epsf.tex when
using plain TeX with dvipdfmx. As in: \input epsf \input epsf-dvipdfmx
It is needed when an .eps file has anything except the origin (0,0) for
the lower-left of its bounding box.

