echo "============"
echo "Script to Collect Stattistic result From NonLinLoc - Global mode ==>> INPUT HYPODD"
echo "Developed by Arham Zakki Edelo TG-ITS"
echo "Email_1: azedelo1999@gmail.com"
echo "Email_2: edelo.arham@gmail.com"
echo
echo "IMPORTANT"
echo "   1. Taruh script run_HD.SH dan Script COLLECT_HYPODD.py ini pada directory yang sama dengan data yang akan di collect (hasil NonLinLoc)"
echo "   2. Harus terinstall python3 dengan library pandas "
echo

#PS_VIEWER=ghostview

echo
python3 ./COLLECT_HYPODD.py

echo "!!!!NOTE!!!!!!"
echo "  1. SETELAH INI WAJIB GANTI NILAI PEMBOBOTAN PADA FILE EXCEL, DAN MENYESUAIKAN KEMBALI FORMAT SESUAI DENGAN HYPODD"
echo "  2. DISARANKAN MENGGUNAKAN TEXT EDITOR SEPERTI KATE, SUBLIME TEXT, NOTEPAD++, ATOM, DLL"
echo "  3. PROSES FIND & REPLACE DENGAN TEXT EDITOR SERTA PENYESUAIAN FORMAT HARUS SESUAI DENGAN FORNAT DI USERGUIDE HYPODD"
