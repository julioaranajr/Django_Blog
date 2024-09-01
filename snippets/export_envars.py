import os

# def export_env_vars(env_vars):
#     """
#     Export environment variables to the OS profile.
    
#     Args:
#         env_vars (dict): A dictionary containing the environment variables to export.
#     """
#     for key, value in env_vars.items():
#         os.environ[key] = value
        
#     print('Environment variables exported successfully.')
    
# # Define the environment variables to export

# env_vars = {
#     'SECRET_KEY': 'mysecretkey',
#     'EMAIL_USER': 'user@example.com',
#     'EMAIL_PASS': 'password',
#     'DB_USER': 'db_user',
#     'DB_PASS': 'db_password'
# }

# # Export the environment variables
# export_env_vars(env_vars)

def read_os_profile():
    """
    Read and print the OS profile.
    """
    for key, value in os.environ.items():
        print(f"{key}: {value}")
        
# # Read and print the OS profile
read_os_profile()

# Unset specific variables in the environment variables file
# def unset_env_vars(env_vars):
#     """
#     Unset environment variables in the OS profile.
    
#     Args:
#         env_vars (list): A list of environment variables to unset.
#     """
#     for var in env_vars:
#         os.environ.pop(var, None)
        
#     print('Environment variables unset successfully.')
    
# # Define the environment variables to unset
# env_vars_to_unset = ['SECRET_KEY', 'EMAIL_USER', 'EMAIL_PASS', 'DB_USER', 'DB_PASS']