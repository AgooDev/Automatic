# packages required
import shutil
import os


# Global functions
# Check if folder exists
def folder_exists(path):
    exists = False
    dir = os.path.dirname(path)
    if os.path.exists(dir):
        exists = True
    return exists


# Create index.php basic file
def create_index_php(path):
    php_code = """
    <?php
        // Silence is golden.
        header( 'Location: http://www.agoo.com.co/404' ) ;
    ?>
    """
    file_path = path + "/index.php"
    php_file = open(file_path)
    php_file.write(php_code)
    php_file.close()


# Create folder
def create_folder:


# Delete folder
def delete_folder():
    return True