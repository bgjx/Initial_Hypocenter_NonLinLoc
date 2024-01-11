echo "============"
echo "Script to run sample locations for NonLinLoc - Global mode"
echo "see http://alomax.net/nlloc"
echo "uses phase data from NEIC"
echo
echo "IMPORTANT:  Requires:"
echo "   1. NonLinLoc - the command \"NLLoc\" must be on your path"
echo "   2. Java - the command \"java\" must be on your path (Java version 1.8 or later)"
echo "   3. The TauPToolkit - see http://www.seis.sc.edu/software/TauP and the Java class edu.sc.seis.TauP.TauP_Table_NLL - see http://alomax.net/nlloc/java."
echo "      or the Java archive TauP_NLL.jar on your java classpath - see http://alomax.net/nlloc/java."
echo "   4. SeismicityViewer must be installed and on your java classpath - see: http://alomax.net/seismicity"
echo "   5. The environment variable PS_VIEWER is set in your shell or in this script"
echo

#PS_VIEWER=ghostview

echo
echo Create spherical, layered-model, travel-time grids for NonLinLoc
dirku=taup
#setenv CLASSPATH ./$(taup)/TauP_NLL.jar:$(/home/arhamze/SEMESTER_7/MEQ)/SeismicityViewer.jar	# support /bin/sh
export CLASSPATH=./$(dirku)/TauP_NLL.jar #:$()/SeismicityViewer.jar	# support /bin/bash
#echo "CLASSPATH=${CLASSPATH}"
cd taup
./TauP_Table_NLL.sh
echo
#echo Visualize P travel-time grid
#./plot_time.gmt.sh
#${PS_VIEWER} ak135/ak135.P.DEFAULT.time.ps &
cd ..

echo
echo Run NonLinLoc
/home/arhamze/SEMESTER_7/MEQ/NonLinLoc_master/src/bin/NLLoc run/neic_global.in

echo
echo Visualize each location in SeismicityViewer
java -jar /home/arhamze/SEMESTER_7/MEQ/SeismicityViewer50.jar loc/sunda.*.*.grid0.loc.hyp
#java -jar /home/arhamze/SEMESTER_7/MEQ/SeismicityViewer50.jar loc/global.20031210.*.grid0.loc.hyp
#java -jar /home/arhamze/SEMESTER_7/MEQ/SeismicityViewer50.jar loc/global.20031214.*.grid0.loc.hyp
#java -jar /home/arhamze/SEMESTER_7/MEQ/SeismicityViewer50.jar loc/global.20040224.*.grid0.loc.hyp
#java -jar /home/arhamze/SEMESTER_7/MEQ/SeismicityViewer50.jar loc/global.20060717.*.grid0.loc.hyp
