'''
paramiko ssh example.

Reference:
    - https://ithelp.ithome.com.tw/articles/10245205
'''

import paramiko


def ssh_command(hostname, port, username, password, command):
    # Initialize the SSH client
    ssh = paramiko.SSHClient()

    # Automatically add the server's SSH key (make sure you trust the server)
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        # Connect to the server
        ssh.connect(hostname, port, username, password)

        # Execute a command (e.g., 'ls' to list directory contents)
        stdin, stdout, stderr = ssh.exec_command(command)

        # Read the output from stdout
        output = stdout.read().decode()
        print("Command output:")
        print(output)

        # Read the error from stderr (if any)
        error = stderr.read().decode()
        if error:
            print("Command error:")
            print(error)

    except paramiko.AuthenticationException:
        print("Authentication failed.")
    except paramiko.SSHException as sshException:
        print(f"Unable to establish SSH connection: {sshException}")
    except Exception as e:
        print(f"Exception in connecting to the server: {e}")
    finally:
        # Close the connection
        ssh.close()

if __name__ == '__main__':
    # Define the server and login details
    hostname = 'your.server.com'
    port = 22
    username = 'your_username'
    password = 'your_password'  # Use key-based authentication for better security
    command = 'ls'

    ssh_command(hostname, port, username, password, command)
