#!/usr/bin/perl

print "Content-type: text/html\n\n";

$g = "<title>";

$bootdir = '/home/users/rh/public_html/bootleg';

if ($ENV{'REQUEST_METHOD'} ne "GET") { &wrong_invoke; }

$srh = $ENV{'QUERY_STRING'};

opendir(BDIR, $bootdir) || die "Can't find bootleg directory!";
@files = readdir(BDIR);
closedir BDIR;

print @files;

foreach $fname (@files)
{
 open (SERCH, $bootdir.'/'.$fname);
 $ts = "";
 if (($fname ne "bootlegs.html") && !($fname =~ /gif/)) {
 while (<SERCH>)
  {
   if (/$g/) { $ts += $_; }
   push @results, $fname if /$srh/i;
  }
 }
 close SERCH;
}

open TITLES, "bootlegs.html";
while (<TITLES>)
{
foreach $s (@results) {
 if (/$s/) {
  s/<.*?>//g;
  s/\s*//;
  s/(&nbsp;)//g;
  push @code, qq*<a href="$s">$_</a><br>\n*;
 }
 }
}
close TITLES;

print <<EOF;
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2//EN">
<HTML>
<HEAD>
   <TITLE>Bootlegs</TITLE>
      <META HTTP-EQUIV="Content-Type" CONTENT="text/html; charset=iso-8859-1">
         </HEAD>
         <BODY TEXT="#FFFFFF" BGCOLOR="#000000" LINK="#3333FF" VLINK="#33CCFF" ALINK="#FF0000">

         <CENTER><P><IMG SRC="bootlegs.gif" HEIGHT=39 WIDTH=220> </P></CENTER>

         <CENTER><P><B><FONT SIZE=+2>S</FONT>EARCH<FONT SIZE=+2>&nbsp;R</FONT>ESULTS</B><BR> for "<TT>$srh</TT>"<BR>
         </P></CENTER>
EOF
print @code;
print <<EOF;


         <CENTER><P><A HREF="bootlegs.html">Back to bootleg index</A></P></CENTER>

         </BODY>
         </HTML>
EOF

exit;


sub wrong_invoke {
print "dx";

print <<EOF;
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2//EN">
<HTML>
<HEAD>
   <TITLE>Bootlegs</TITLE>
      <META HTTP-EQUIV="Content-Type" CONTENT="text/html; charset=iso-8859-1">
         </HEAD>
         <BODY TEXT="#FFFFFF" BGCOLOR="#000000" LINK="#3333FF" VLINK="#33CCFF" ALINK="#FF0000">
<FONT SIZE=+3><B>ERROR!</B></FONT>
<P>This script has been used wrongly. Press 'Back' on your browser to go back.</P>
         </BODY>
         </HTML>
EOF


exit;
}
