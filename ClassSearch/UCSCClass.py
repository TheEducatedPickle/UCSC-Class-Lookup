import os
import requests
import re

class UCSCClass:
    def __init__(self,html):    
        splitr = '<div class="col-xs-12 col-sm-6 col-md-6" >(.*?)</div>'
        isor = '<dd>(.*?)</dd>'

        html = html.replace('\n','')
        tbls = re.findall(splitr,html)#Split table to left and right side
        leftmatches = re.findall(isor,tbls[0])
        rightmatches = re.findall(isor,tbls[1])    

        self.career = leftmatches[0]
        self.grading = leftmatches[1]
        self.classNum = leftmatches[2]
        self.type = leftmatches[3]
        self.credits = leftmatches[4]
        self.genEd = leftmatches[5] if leftmatches[5] != '&nbsp;' else None
        self.status = "Open" if "Open" in rightmatches[0][:-7] else "Closed" if "Closed" in rightmatches[0][:-7] else "Waitlist"
        self.availibleSeats = rightmatches[1][:-7]
        self.enrollCap = rightmatches[2][:-7]
        self.enrolled = rightmatches[3][:-7]
        self.waitlistCap = rightmatches[4][:-7]
        self.waitlistTotal = rightmatches[5][:-7]
        print(self.career, self.grading,self.waitlistCap)
class Section:
    req = requests.Request("POST", "https://pisa.ucsc.edu/class_search/index.php")


testHTML = """<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
	<html xmlns="http://www.w3.org/1999/xhtml" lang="en" xml:lang="en">
	<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
	<meta http-equiv="Content-Type" content="text/html;" />
	<title>UC Santa Cruz - Schedule of Classes</title>
	<link rel="stylesheet" type="text/css" href="https://ajax.googleapis.com/ajax/libs/jqueryui/1.11.4/themes/smoothness/jquery-ui.css" />
	<link rel="stylesheet" type="text/css" href="https://pisa.ucsc.edu/cs9/prd/stylesheets/soc.css" />
	<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css" integrity="sha384-1q8mTJOASx8j1Au+a5WDVnPi2lkFfwwEAa8hDDdjZlpLegxhjVME1fgjWPGmkzs7" crossorigin="anonymous">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/font-awesome/4.6.1/css/font-awesome.min.css">

<style>
.row-striped:nth-of-type(even){
  background-color: #EEF5FB;
}

.row-striped:nth-of-type(odd){
  background-color: #ffffff;
}
.panel-default > .panel-heading-custom{
  background-image: none;
  background-color: #EEF5FB;
  color: #31708f;
}
.panel-default > .panel-heading-custom > h4{
  margin-top     : 0px;
  margin-bottom  : 0px;
}
@media print {
  * { background: transparent !important; color: black !important; text-shadow: none !important; filter:none !important; -ms-filter: none !important; } /* Black prints faster: h5bp.com/s */
  a, a:visited { text-decoration: none; }
 a[href]:after { content: ""  !important; }
  abbr[title]:after { content: ""  !important; }
  .ir a:after, a[href^="javascript:"]:after, a[href^="#"]:after { content: ""  !important; }
   pre, blockquote { border: 1px solid #999; page-break-inside: avoid; }
  thead { display: table-header-group; } /* h5bp.com/t */
  tr, img { page-break-inside: avoid; }
  img { max-width: 100% !important; }
  @page { margin: 0.5cm; }
  p, h2, h3 { orphans: 3; widows: 3; }
  h2, h3 { page-break-after: avoid; }
  .row { page-break-inside: avoid; }
  .hide-print {display: none; }
  .panel {border: 0px; max-width: none !important; }
}


.dl-horizontal dt {
  float: left;
  width: 160px;
  overflow: hidden;
  clear: left;
  text-align: right;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.dl-horizontal dd {
  margin-left: 180px;
}
</style>

<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.min.js" type="text/javascript"></script>
<script src="https://ajax.googleapis.com/ajax/libs/jqueryui/1.11.4/jquery-ui.min.js" type="text/javascript"></script>
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/js/bootstrap.min.js" integrity="sha384-0mSbJDEHialfmuBBQP6A4Qrprq5OVfW37PRR3j5ELqxss1yVqOtnepnHVP9aJ7xS" crossorigin="anonymous"></script>
	<!--INC0448957 - JM - Accessibility: To have skip nav working -->
	<script type="text/javascript">
	document.domain = "ucsc.edu";
	parent.document.title = document.title;
	</script><script type="text/javascript" src="https://pisa.ucsc.edu/cs9/prd/sr9_2013/js/results.js"></script><script>  $(  function() {
							$("#search_box").init_search_dialog('detail');
							$("#search_link, #search_link_bot").click( function() { $("#search_box").dialog('open') });

					    }
					);
	      </script><script type="text/javascript" src="https://pisa.ucsc.edu/cs9/prd/sr9_2013/js/search.js"></script><script>$(
					function() {
						on_term_init($("#term_dropdown").val());
						$("#crse_units_op").showHide_crse_units();
						$("#search_anchor").focus();
						$("#term_dropdown").change(
							function() {
								on_term_change($("#term_dropdown").val());					}
						 );
						$("#crse_units_op").change(
							function() { $("#crse_units_op").showHide_crse_units(); }
						);
						$("#search_button").click(
							  function() {
							  if ( validate_input_count() ) {
							  		$("#searchForm").submit();
							  } else {
							  		return false;
							  }
							}
						)
					}
				   );
		  </script><noscript><meta http-equiv="refresh" content="0; URL=https://pisa.ucsc.edu/cs9/prd/sr9_2013/enable_javascript.php"></noscript>
	</head>

	<body><div>
<div id = "search_box" style="display: none;" title="Search">
    


<form action="index.php" method="post" name="searchForm" id="searchForm">
<input type = "hidden" name = "action" value = "results" />






<!-- Term -->

<div class="form-group row">
  <!--td align="right" class="PSDROPDOWNLABEL" style="width:20%" -->
<label for="term_dropdown" class="col-sm-2 form-control-label"><b>Term</b></label>
 <div class="col-sm-10">
    <select name = "binds[:term]" id = "term_dropdown" class="form-control">
    <option value = "2194" >2019 Summer Quarter</option><option value = "2192"  selected="selected">2019 Spring Quarter</option><option value = "2190" >2019 Winter Quarter</option><option value = "2188" >2018 Fall Quarter</option><option value = "2184" >2018 Summer Quarter</option><option value = "2182" >2018 Spring Quarter</option><option value = "2180" >2018 Winter Quarter</option><option value = "2178" >2017 Fall Quarter</option><option value = "2174" >2017 Summer Quarter</option><option value = "2172" >2017 Spring Quarter</option><option value = "2170" >2017 Winter Quarter</option><option value = "2168" >2016 Fall Quarter</option><option value = "2164" >2016 Summer Quarter</option><option value = "2162" >2016 Spring Quarter</option><option value = "2160" >2016 Winter Quarter</option><option value = "2158" >2015 Fall Quarter</option><option value = "2154" >2015 Summer Quarter</option><option value = "2152" >2015 Spring Quarter</option><option value = "2150" >2015 Winter Quarter</option><option value = "2148" >2014 Fall Quarter</option><option value = "2144" >2014 Summer Quarter</option><option value = "2142" >2014 Spring Quarter</option><option value = "2140" >2014 Winter Quarter</option><option value = "2138" >2013 Fall Quarter</option><option value = "2134" >2013 Summer Quarter</option><option value = "2132" >2013 Spring Quarter</option><option value = "2130" >2013 Winter Quarter</option><option value = "2128" >2012 Fall Quarter</option><option value = "2124" >2012 Summer Quarter</option><option value = "2122" >2012 Spring Quarter</option><option value = "2120" >2012 Winter Quarter</option><option value = "2118" >2011 Fall Quarter</option><option value = "2114" >2011 Summer Quarter</option><option value = "2112" >2011 Spring Quarter</option><option value = "2110" >2011 Winter Quarter</option><option value = "2108" >2010 Fall Quarter</option><option value = "2104" >2010 Summer Quarter</option><option value = "2102" >2010 Spring Quarter</option><option value = "2100" >2010 Winter Quarter</option><option value = "2098" >2009 Fall Quarter</option><option value = "2094" >2009 Summer Quarter</option><option value = "2092" >2009 Spring Quarter</option><option value = "2090" >2009 Winter Quarter</option><option value = "2088" >2008 Fall Quarter</option><option value = "2084" >2008 Summer Quarter</option><option value = "2082" >2008 Spring Quarter</option><option value = "2080" >2008 Winter Quarter</option><option value = "2078" >2007 Fall Quarter</option><option value = "2074" >2007 Summer Quarter</option><option value = "2072" >2007 Spring Quarter</option><option value = "2070" >2007 Winter Quarter</option><option value = "2068" >2006 Fall Quarter</option><option value = "2064" >2006 Summer Quarter</option><option value = "2062" >2006 Spring Quarter</option><option value = "2060" >2006 Winter Quarter</option><option value = "2058" >2005 Fall Quarter</option><option value = "2054" >2005 Summer Quarter</option><option value = "2052" >2005 Spring Quarter</option><option value = "2050" >2005 Winter Quarter</option><option value = "2048" >2004 Fall Quarter</option>    </select>
 </div>
</div>


<!-- Session -->
<div class="form-group row">
<label for="Session" class="col-sm-2 form-control-label"><b>Session</b></label>
 <div class="col-sm-10">
    <select name = "binds[:session_code]" id = "Session" class="form-control form-control-sm">
        <option value = "" selected="selected">All Sessions</option>

        <option value = "ED1">Education Masters, Fifth Qtr</option><option value = "ED2">Education Masters, First Qtr</option><option value = "1">Regular Academic Session</option><option value = "5S1">Summer Session 1 (5 Weeks)</option><option value = "S10">Summer Session 10 Weeks</option><option value = "5S2">Summer Session 2 (5 Weeks)</option><option value = "S8W">Summer Session 8 Weeks</option>
    </select>
 </div>
</div>

<!-- Reg Status -->
<div class="form-group row">
<label for="reg_status" class="col-sm-2 form-control-label"><b>Status</b></label>
 <div class="col-sm-10">
    <select name = "binds[:reg_status]" id="reg_status" class="form-control form-control-sm">
        <option value = "O">Open Classes</option><option value = "all" selected="selected">All Classes</option>     </select>
 </div>
</div>

<!-- Subject -->
<div class="form-group row">
<label for="subject" class="col-sm-2 form-control-label"><b>Subject</b></label>
 <div class="col-sm-10">
    <select name = "binds[:subject]" id = "subject" class="form-control form-control-sm" placeholder="Select">
        <option value = ""  selected="selected">&nbsp;</option>
        <option value = "" >All Subjects</option>
        <option value = "ACEN">Academic English</option><option value = "AMST">American Studies</option><option value = "ANTH">Anthropology</option><option value = "APLX">Applied Linguistics</option><option value = "AMS">Applied Math and Statistics</option><option value = "ARAB">Arabic</option><option value = "ART">Art</option><option value = "ARTG">Art&Des:Games&PlayableMedia</option><option value = "ASTR">Astronomy and Astrophysics</option><option value = "BIOC">Biochemistry and Molecular Bio</option><option value = "BIOL">Biology: Molecular Cell & Dev</option><option value = "BIOE">Biology:Ecology & Evolutionary</option><option value = "BME" selected="selected">Biomolecular Engineering</option><option value = "CRSN">Carson College</option><option value = "CHEM">Chemistry and Biochemistry</option><option value = "CHIN">Chinese</option><option value = "CSP">Coastal Science and Policy</option><option value = "CLEI">College Eight</option><option value = "CLNI">College Nine</option><option value = "CLTE">College Ten</option><option value = "CMMU">Community Studies</option><option value = "CMPM">Computational Media</option><option value = "CMPE">Computer Engineering</option><option value = "CMPS">Computer Science</option><option value = "COWL">Cowell College</option><option value = "LTCR">Creative Writing</option><option value = "CRES">Critical Race & Ethnic Studies</option><option value = "CRWN">Crown College</option><option value = "DANM">Digital Arts and New Media</option><option value = "EART">Earth Sciences</option><option value = "ECON">Economics</option><option value = "EDUC">Education</option><option value = "EE">Electrical Engineering</option><option value = "ENGR">Engineering</option><option value = "LTEL">English-Language Literatures</option><option value = "ESCI">Environmental Sciences</option><option value = "ENVS">Environmental Studies</option><option value = "ETOX">Environmental Toxicology</option><option value = "FMST">Feminist Studies</option><option value = "FILM">Film and Digital Media</option><option value = "FREN">French</option><option value = "LTFR">French Literature</option><option value = "GAME">Games and Playable Media</option><option value = "GERM">German</option><option value = "LTGE">German Literature</option><option value = "GREE">Greek</option><option value = "LTGR">Greek Literature</option><option value = "HEBR">Hebrew</option><option value = "HNDI">Hindi</option><option value = "HIS">History</option><option value = "HAVC">History of Art&Visual Culture</option><option value = "HISC">History of Consciousness</option><option value = "HUMN">Humanities</option><option value = "ISM">Information Systems Management</option><option value = "ITAL">Italian</option><option value = "LTIT">Italian Literature</option><option value = "JAPN">Japanese</option><option value = "JWST">Jewish Studies</option><option value = "KRSG">Kresge College</option><option value = "LAAD">Languages</option><option value = "LATN">Latin</option><option value = "LALS">Latin American&Latino Studies</option><option value = "LTIN">Latin Literature</option><option value = "LGST">Legal Studies</option><option value = "LING">Linguistics</option><option value = "LIT">Literature</option><option value = "MATH">Mathematics</option><option value = "MERR">Merrill College</option><option value = "METX">Microbiol & Environ Toxicology</option><option value = "LTMO">Modern Literary Studies</option><option value = "MUSC">Music</option><option value = "OAKS">Oakes College</option><option value = "OCEA">Ocean Sciences</option><option value = "PHIL">Philosophy</option><option value = "PBS">Physical & Biological Sciences</option><option value = "PHYE">Physical Education</option><option value = "PHYS">Physics</option><option value = "POLI">Politics</option><option value = "PRTR">Porter College</option><option value = "PORT">Portuguese</option><option value = "LTPR">Pre & Early Modern Literature</option><option value = "PSYC">Psychology</option><option value = "PUNJ">Punjabi</option><option value = "RUSS">Russian</option><option value = "SCIC">Science Communication</option><option value = "SOCD">Social Documentation</option><option value = "SOCS">Social Sciences</option><option value = "SOCY">Sociology</option><option value = "SPAN">Spanish</option><option value = "SPHS">Spanish for Heritage Speakers</option><option value = "SPSS">Spanish for Spanish Speakers</option><option value = "LTSP">Spanish/Latin Amer/Latino Lit</option><option value = "STEV">Stevenson College</option><option value = "TIM">Technology & Info Management</option><option value = "THEA">Theater Arts</option><option value = "UCDC">UCDC</option><option value = "WMST">Women's Studies</option><option value = "LTWL">World Lit & Cultural Studies</option><option value = "WRIT">Writing</option><option value = "YIDD">Yiddish</option>    </select>
 </div>
</div>


<!-- Course Number -->
<div class="form-group row">
<label for="catalog_nbr" class="col-sm-2 form-control-label"><b>Course Number</b></label>
 <div class="col-sm-10">
 <label for="catalog_nbr_fltr" class="sr-only">Class Number Filter</label>
 <div class="col-sm-6" style="margin-left: 0px; padding-left: 0px;">
        <select id="catalog_nbr_fltr" name = "binds[:catalog_nbr_op]"  class="form-control form-control-sm">
            <option value ="=" selected="selected">is exactly</option><option value ="contains">contains</option><option value ="<=">less than or equal to</option><option value =">=">greater than or equal to</option>        </select>
  </div>
  <div class="col-sm-6" style="margin-right: 0px; padding-right: 0px;">
     <input type = "text"  placeholder="Course #" class="form-control form-control-sm" maxlength = "5" name = "binds[:catalog_nbr]" id = "catalog_nbr" value = "" />
 </div>
 </div>
</div>

<!-- Class Title -->
<div class="form-group row">
<label for="title" class="col-sm-2 form-control-label"><b>Course Title Keyword</b></label>
 <div class="col-sm-10">
    <input type = "text" class="form-control form-control-sm" maxlength = "50" name = "binds[:title]" id="title" value = "" />
 </div>
</div>

<!-- Instructor -->
<div class="form-group row">
<label for="instructor" class="col-sm-2 form-control-label"><b>Instructor Last Name</b></label>
 <div class="col-sm-10">
 <div class="col-sm-6" style="margin-left: 0px; padding-left: 0px;">
 <label for="instructor_fltr" class="sr-only">Instructer Filter</label>
  <select id="instructor_fltr" name = "binds[:instr_name_op]" class="form-control form-control-sm">
        <option value ="=" selected="selected">is exactly</option><option value ="contains">contains</option><option value ="begins">begins with</option>  </select>
  </div>
  <div class="col-sm-6" style="margin-right: 0px; padding-right: 0px;">
     <input type = "text" class="form-control form-control-sm" placeholder="Last Name" maxlength = "50" name = "binds[:instructor]" id="instructor" value = ""/>
 </div>
 </div>
</div>

<!-- Geneds -->
<div class="form-group row">
<label for="ge" class="col-sm-2 form-control-label"><b>General Education</b></label>
 <div class="col-sm-10">
    <select name = "binds[:ge]" id="ge" placeholder="Select" class="form-control form-control-sm">
    <option value="">&nbsp;</option>

    <option value = "A">A</option><option value = "C">C</option><option value = "C1">C1</option><option value = "C2">C2</option><option value = "CC">CC</option><option value = "E">E</option><option value = "ER">ER</option><option value = "IH">IH</option><option value = "IM">IM</option><option value = "IN">IN</option><option value = "IS">IS</option><option value = "MF">MF</option><option value = "PE-E">PE-E</option><option value = "PE-H">PE-H</option><option value = "PE-T">PE-T</option><option value = "PR-C">PR-C</option><option value = "PR-E">PR-E</option><option value = "PR-S">PR-S</option><option value = "Q">Q</option><option value = "SI">SI</option><option value = "SR">SR</option><option value = "TA">TA</option><option value = "TH">TH</option><option value = "TN">TN</option><option value = "TS">TS</option><option value = "W">W</option><option value = "AnyGE">Any Requirement</option>
    </select>
 </div>
</div>

<!-- Course Units -->
<div class="form-group row">
<label for="crse_units_exact" class="col-sm-2 form-control-label"><b>Course Units</b></label>
<label for="crse_units_op" class="sr-only">Course Units Filter</label>

 <div class="col-sm-10">
 <div class="col-sm-6" style="margin-left: 0px; padding-left: 0px;">
        <select class="form-control form-control-sm" name = "binds[:crse_units_op]" id="crse_units_op">
            <option value ="=" selected="selected">is exactly</option><option value ="between">between</option>        </select>
  </div>
      <div id="crse_units_between" class="col-sm-6" style="display:none; margin-right: 0px; padding-right: 0px;">
          <input type = "text" class="form-control form-control-sm" maxlength = "2" name = "binds[:crse_units_from]" id="crse_units_from" placeholder="Units From" value = "" />
            and <input type = "text" class="form-control form-control-sm" maxlength = "2" name = "binds[:crse_units_to]" id="crse_units_to" placeholder="Units To" value = "" />
      </div>
      <div id="crse_units_exact_div" class="col-sm-6"  style="margin-right: 0px; padding-right: 0px;">
          <input type = "text" class="form-control form-control-sm" maxlength = "2" name = "binds[:crse_units_exact]" id="crse_units_exact" placeholder="Units" value = "" />
      </div>
      </div>
</div>

<!-- Meeting Days -->
<div class="form-group row">
<label for="Days" class="col-sm-2 form-control-label"><b>Meeting Days</b></label>
 <div class="col-sm-10">
    <select name = "binds[:days]" id = "Days" class="form-control form-control-sm">
        <option value="">&nbsp;</option>
        <option value="">All Days</option>
        <option value = "MTWR">MTuWTh</option><option value = "MTWRF">MTuWThF</option><option value = "MWF">MWF</option><option value = "MW">MW</option><option value = "TWR">TuWTh</option><option value = "TR">TuTh</option><option value = "M">M</option><option value = "T">T</option><option value = "W">W</option><option value = "R">Th</option><option value = "F">F</option>    </select>
 </div>
</div>

<!-- Meeting Times -->
<div class="form-group row">
<label for="Times" class="col-sm-2 form-control-label"><b>Meeting Times</b></label>
 <div class="col-sm-10">
    <select name = "binds[:times]" id = "Times"  class="form-control form-control-sm">
        <option value="">&nbsp;</option>
        <option value="">All Times</option>
        <option value = "Morning">Morning</option><option value = "Afternoon">Afternoon</option><option value = "Evening">Evening</option><option value = "08:00AM09:05AM">0800AM - 0905AM</option><option value = "08:00AM09:35AM">0800AM - 0935AM</option><option value = "09:20AM10:25AM">0920AM - 1025AM</option><option value = "09:50AM11:25AM">0950AM - 1125AM</option><option value = "10:40AM11:45AM">1040AM - 1145AM</option><option value = "11:40AM01:15PM">1140AM - 0115PM</option><option value = "12:00PM01:05PM">1200PM - 0105PM</option><option value = "01:20PM02:25PM">0120PM - 0225PM</option><option value = "01:30PM03:05PM">0130PM - 0305PM</option><option value = "02:40PM03:45PM">0240PM - 0345PM</option><option value = "03:20PM04:55PM">0320PM - 0455PM</option><option value = "04:00PM05:05PM">0400PM - 0505PM</option><option value = "05:20PM06:55PM">0520PM - 0655PM</option><option value = "07:10PM08:45PM">0710PM - 0845PM</option><option value = "08:00PM09:45PM">0800PM - 0945PM</option>    </select>
 </div>
</div>

<!-- Career -->
<div class="form-group row">
<label for="acad_career" class="col-sm-2 form-control-label"><b>Course Career</b></label>
 <div class="col-sm-10">
    <select name = "binds[:acad_career]" id="acad_career" class="form-control form-control-sm">
    <option value = ""  selected="selected">&nbsp;</option>
    <option value = "" >Any</option>
    <option value = "UGRD">Undergraduate</option><option value = "GRAD">Graduate</option>    </select>
 </div>
</div>

<!-- Online Only -->
<div class="row">
<div class="col-sm-10">
<div class="checkbox">
  <label>
    <input type="checkbox" name="binds[:online_only]" id="online_only" value="1">
    Show Online Classes Only  </label>
</div>
</div>
</div>

<p>


</div>
</form>
</div>

<div id = "back" style="display: none;">
  <form id="back_form" name="back_form" action="index.php" method="post">
            <input type="hidden" name="binds[:term]" value="2192">
            <input type="hidden" name="binds[:reg_status]" value="all">
            <input type="hidden" name="binds[:subject]" value="BME">
            <input type="hidden" name="binds[:catalog_nbr_op]" value="=">
            <input type="hidden" name="binds[:catalog_nbr]" value="">
            <input type="hidden" name="binds[:title]" value="">
            <input type="hidden" name="binds[:instr_name_op]" value="=">
            <input type="hidden" name="binds[:instructor]" value="">
            <input type="hidden" name="binds[:ge]" value="">
            <input type="hidden" name="binds[:crse_units_op]" value="=">
            <input type="hidden" name="binds[:crse_units_from]" value="">
            <input type="hidden" name="binds[:crse_units_to]" value="">
            <input type="hidden" name="binds[:crse_units_exact]" value="">
            <input type="hidden" name="binds[:days]" value="">
            <input type="hidden" name="binds[:times]" value="">
            <input type="hidden" name="binds[:acad_career]" value="">
            <input type="hidden" name="binds[:session_code]" value="">
            <input type="hidden" name="action" value="results">
      <input type="hidden" name="rec_start" value="0">
      <input type="hidden" name="rec_dur" value="25">
      <input type="hidden" name="resume" value="1">
  </form>
</div>

<div class="panel panel-info center-block" style="max-width: 900px;">
         <div class="panel-heading"><H1 style="display:inline-block;"><i class="fa fa-search fa-pull-left" aria-hidden="true"></i>
          Class Detail
         </H1><img src="./logo.png" style="float: right;" alt="UCSC Logo">
        <div style="clear:both;"></div>
         </div>
         <div class="panel-body">

<div class='row'>
    <div class="col-xs-12">
     <h2 style="margin:0px;">
        BME 21L - 01&nbsp;&nbsp; Introduction to Basic Laboratory Techniques    </h2>
    </div>
</div>
    <div class='row'>
        <div class="col-xs-6" >
            2019 Spring Quarter<br /><br />
                            <a class="hide-print" id="back_link" href="javascript:void(0)" onclick="document.back_form.submit(); return false;"><i class="fa fa-arrow-left" aria-hidden="true"></i>  Back to results</a> <br />
                        <a class="hide-print" href = "index.php"><i class="fa fa-search" aria-hidden="true"></i> Search</a>
            <p />
        </div>
        <div class="col-xs-6" >
            <div style="float:right;" class="hide-print">
            <div style="display:none;" id="directUrl">https://pisa.ucsc.edu/class_search/index.php?action=detail&class_data=YToyOntzOjU6IjpTVFJNIjtzOjQ6IjIxOTIiO3M6MTA6IjpDTEFTU19OQlIiO3M6NToiNjI5ODMiO30%253D</div><br /><br />
                  <a href="https://pisa.ucsc.edu/class_search/index.php?action=detail&class_data=YToyOntzOjU6IjpTVFJNIjtzOjQ6IjIxOTIiO3M6MTA6IjpDTEFTU19OQlIiO3M6NToiNjI5ODMiO30%253D" onclick="copyToClipboard('#directUrl'); return false;"><i class="fa fa-files-o" aria-hidden="true"></i> Copy Link</a><br>

                  <a href="http://ucsc.verbacompare.com/comparison?id=SP19__BME__021L__01" target="_blank"><i class="fa fa-book" aria-hidden="true"></i> Materials</a>
                                    <p />
            </div>
        </div>
    </div>
      <div class="panel-group">
        <div class="panel panel-default row">
          <div class="panel-heading panel-heading-custom"><h2 style="margin:0px;">Class Details</h2></div>
          <div class="panel-body">

            <div class='row'>
                <div class="col-xs-12 col-sm-6 col-md-6" >
                    <dl class="dl-horizontal" style="margin-bottom: 0px;">
                        <dt>Career</dt><dd>Undergraduate</dd>
                        <dt>Grading</dt><dd>Student Option</dd>
                        <dt>Class Number</dt><dd>62983</dd>
                        <dt>Type</dt><dd>Laboratory</dd>
                        <dt>Credits</dt><dd>5 units</dd>
                        <dt>General Education</dt><dd>&nbsp;</dd>
                    </dl>
                </div>
                <div class="col-xs-12 col-sm-6 col-md-6" >
                    <dl class="dl-horizontal" style="margin-bottom: 0px;">
                        <dt>Status</dt><dd><img src="https://pisa.ucsc.edu/cs9/prd/images/PS_CS_STATUS_OPEN_ICN_1.gif" alt="Open" title="Open"  aria-hidden="true"> Open</span></dd>
                        <dt>Available Seats</dt><dd>8</span></dd>
                        <dt>Enrollment Capacity</dt><dd>24</span></dd>
                        <dt>Enrolled</dt><dd>16</span></dd>
                        <dt>Wait List Capacity</dt><dd>0</span></dd>
                        <dt>Wait List Total</dt><dd>0</span></dd>
                    </dl>
                </div>
            </div>
          </div>
        </div>


        
        <div class="panel panel-default row">
          <div class="panel-heading panel-heading-custom"><h2 style="margin:0px;">Description</h2></div>
          <div class="panel-body">
            Introduces students to basic laboratory techniques that are essential to begin work in faculty research labs and on capstone projects. Students have several independent blocks/fixed projects and learn how to use various instruments and techniques employed in biotechnology laboratories, such as: calibration and use of the pipette; making up various buffers; pH titration; Bactrial transformation; TAcloning; plasmid and DNA isolation; Polymerase Chain Reaction (PCR); gel electrophoresis; Pyrosequencing; and an introduction to Linux for DNA sequence analysis.          </div>
        </div>

                <div class="panel panel-default row">
          <div class="panel-heading panel-heading-custom"><h2 style="margin:0px;">Enrollment Requirements</h2></div>
          <div class="panel-body" >
            Enrollment is restricted to bioengineering, bioinformatics, and biomolecular engineering and bioinformatics majors and proposed majors.          </div>
        </div>
        
        
                <div class="panel panel-default row">
          <div class="panel-heading panel-heading-custom"><h2 style="margin:0px;">Meeting Information</h2></div>
          <div class="panel-body" >
            <table border = "0" cellpadding = "2" width = "100%">
                <tr>
                                        <th scope="col"><strong>Days & Times</strong></th>
                                        <th scope="col"><strong>Room</strong></th>
                                        <th scope="col"><strong>Instructor</strong></th>
                                        <th scope="col"><strong>Meeting Dates</strong></th>
                                    </tr>

                                <tr>
                                            <td>TuTh 03:20PM-04:55PM</td>
                                            <td>J Baskin Engr 301B</td>
                                            <td>Pourmand,N.</td>
                                            <td>04/01/19 - 06/07/19</td>
                                    </tr>
                
            </table>
          </div>
        </div>
        
        
    </div>

    <a class="hide-print" id="back_link" href="javascript:void(0)" onclick="document.back_form.submit(); return false;"><i class="fa fa-arrow-left" aria-hidden="true"></i>  Back to results</a> <br />
    <a class="hide-print" href = "index.php"><i class="fa fa-search" aria-hidden="true"></i> Search</a> <br />

<script type="text/javascript" src="js/detail.js"></script>

</div><script>document.domain='ucsc.edu';</script>
</body>
</html>
"""

if __name__ == "__main__":
    test = UCSCClass(testHTML)