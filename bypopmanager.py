# variable section 
file_types = [0,1]
filename = "evil"
file_extensions = ['.py','.vbs']
file_type_python = 0
file_type_vbs = 1
max_msg_length = 100
file_type_choice = 0
popup_msg = "hello there"
full_filename = ""

# Debug Flag
debug = True

# supporting functions
def create_python_file(fname, message,put_hostname):
	code_import_platform = "import platform\r\n"
	code_import_ctypes = "import ctypes\r\n"
	code_create_hostname = "hostname = \"\\n hostname: \" + platform.node()\r\n"
	code_create_popup_msg = "popup_msg = \"" + message + "\"\r\n"
	code_add_popup_msg_hostname = "popup_msg = popup_msg + hostname\r\n"
	code_invoke_popup_msg = "ctypes.windll.user32.MessageBoxW(0,popup_msg.decode(\"utf-8\", \"ignore\"),\"\",0)\r\n"
	content = ""
	content = content + code_import_platform
	content = content + code_import_ctypes + code_create_hostname + code_create_popup_msg
	#decide whether to print hostname in popup box
	if put_hostname:
		content = content + code_add_popup_msg_hostname
	content = content + code_invoke_popup_msg
	output = open(fname,"w")
	output.write(content)
	print_file_creation_sucess(fname)
	
def create_vbs_file(fname, message,put_hostname):
	code_declare_message = "Dim message\r\n"
	code_declare_hostname = "Dim hostname\r\n"
	code_create_popup_msg = "message = \"" + message + "\"\r\n"
	code_create_hostname = "hostname = vbCrLf + CreateObject(\"WScript.Network\").UserName\r\n"
	code_add_msg_hostname = "message = message + hostname\r\n"
	code_invke_popup_msg = "msgbox(message)\r\n"
	content = ""
	content = content + code_declare_message + code_declare_hostname
	content = content + code_create_popup_msg
	# decide whether to print host name in popup boxs
	if put_hostname:
		content = content + code_create_hostname
		content = content + code_add_msg_hostname
	content = content + code_invke_popup_msg
	output = open(fname,"w")
	output.write(content)
	print_file_creation_sucess(fname)
	
def print_file_creation_sucess(filename):
	print "\n --- successfully created "+ filename + " ---"
	
def print_debug_message(debug_msg):
	if debug:
	   debug_prefix = "\n *debug message* "
	   print debug_prefix + debug_msg
	
# main logic 
def main():
    # asking file type input from user
	file_type_choice = raw_input("Choose file type (number): \n" +
							 "0. python \n" +
							 "1. vbs \n"+
							 "----> ")
	print_debug_message("file type choice was -->" + file_type_choice)
	
	try:
		file_type_choice = int(file_type_choice)
	except:
		print "Invalid file type choice"
		print "Terminating the program"
		exit()
		
	# file type input error handling
	if file_type_choice not in file_types:
		print "Invalid file type choice. Only put resepective file type number from the list"
		print "Terminating the program"
		exit()
	
	# asking pop up message input from user
	popup_msg = raw_input("Input popup message --->")
	
	# pop up message input error handling
	if len(popup_msg) > 100:
		print "Do you really want message that long?"
		print "Terminating the program"
		exit()
		
	print_debug_message("popup message was ---> " + popup_msg) 
	
	put_hostname_choice = raw_input("Print hostname in popup message? (y/n) --->")
	if put_hostname_choice is "y":
		put_hostname = True
	else:
		put_hostname = False

	# getting full file name
	full_filename = filename + str(file_extensions[int(file_type_choice)])
	print_debug_message("full_filename was --> " + full_filename)
	
	# processing user choice and write respecitve output file
	if file_type_choice is file_type_python:
		create_python_file(full_filename, popup_msg,put_hostname=put_hostname)
	elif file_type_choice is file_type_vbs:
		create_vbs_file(full_filename, popup_msg,put_hostname=put_hostname)
	else:
		print "invalid choice. program terminated"

if __name__ == "__main__":
    main()
