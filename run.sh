#!/bin/bash

passdir=passdir
faildir=faildir
FAIL=FAIL
PASS=PASS
faillog=fail.log
passlog=pass.log

function runfail ()
	{
 	grep "$FAIL""[[:space:]]*$" "$resultslog" >> "$faillog"
 	if [ -s "$faillog" ] && [ "$?" -eq 0 ];then
 		echo `date` >> "$faillog" 
 		echo "" >> "$faillog"
  		return 0
 		else
 		return 1
 	fi
	}

function runpass ()
	{
 	grep "$PASS""[[:space:]]*$" "$resultslog" >> "$passlog"
  	if [ -s "$passlog" ] && [ "$?" -eq 0 ];then
		echo `date` >> "$passlog"
		echo "" >> "$passlog"
		return 0
		else
		return 1
	fi
	}

function dirfail()
	{
	find "$dir" -name "*.log" | xargs grep "$FAIL" >> "$faildir"
	if [ -s "$faildir" ] && [ $? -eq 0 ];then
		echo `date` >> "$faildir"
        	echo " " >> "$faildir"	
		return 0
		else
		return 1
	fi
	}

function dirpass ()
	{
	find "$dir" -name "*.log" | xargs grep "$PASS" >> "$passdir"
	if [ -s "$passdir" ] &&[  $? -eq 0 ];then
		echo `date` >> "$passdir"
		echo " " >> "$passdir"
		return 0
		else
		return 1
	fi
	}


function help ()
	{
	echo ""$0 -h" for information"
	echo ""$0" -c for delete files created by the "$0""
	echo ""$0" \"-p -f \"file path\"\" or "$0" \"-f  \"file path\" -p\" for runing"
	echo ""$0" \"-p -d \"directory path\"\" or "$0" \"-d  \"directpry path\" -p\" for runing" 
	}

function h()
	{
	echo ""$0" -h for information"
	}

function fd ()
	{
	if [ "$#" -eq 3 ];then
		case "$1" in
			-p)case "$2" in
				-f) resultslog="$3"
				if [ -s "$resultslog" ];then
					runfail
					runpass
					return 0
					else echo "\""$resultslog"\" not found or is empty"
					return 1
				fi;;
				-d) dir="$3"	
				if [ -d "$dir" ];then
					dirfail
					dirpass
					return 0
					else echo "\""$dir"\" not found or is empty"
					return 1
				fi;;
				 *) h
				    return 1;;
			   esac;;
			-f)case "$3" in
				-p) resultslog="$2"
			             if [ -s "$resultslog" ];then
					runfail
					runpass
					return 0
					else echo ""$resultslog" not found or is empty"
					return 1
                                     fi;;
				 *) h
				    return 1;;
			   esac;;
			-d)case "$3" in
				-p) dir="$2"
		        	    if [ -d "$dir" ];then
				    	dirfail
					dirpass
					return 0
				    	else echo ""$dir" not found or isempty"
					return 1
				    fi;;

				 *) h
				    return 1;;
			   esac;;
			 *)h
			   return 1;;
		esac
	fi
	}

function hc ()
	{
	case "$1" in
		-c) rm -rf "$faillog" "$passlog"
		    rm -rf "$faildir" "$passdir";;	
		-h) help;;
		 *) h
		    return 1;;
	esac	 
	}

function main ()
	{
	if [ "$#" -eq 1 ];then
		hc "$1"
		elif [ "$#" -eq 3 ];then
		fd "$1" "$2" "$3"
		else h
		return 1
	fi
	}

main $@
