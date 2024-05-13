import streamlit as st
import os

# Function to list all files in the "data" folder
def list_files():
    data_folder = "data"
    # Check if the folder exists and is a directory
    files = os.listdir(data_folder) if os.path.exists(data_folder) and os.path.isdir(data_folder) else []
    return files

# Main function to create the PDF Reader app
def main():
    # Set the title of the app
    st.title("PDF Reader")
    
    # Sidebar title
    st.sidebar.title("Files")
    
    # Display files in the sidebar
    files = list_files()
    if files:
        # Create a container for the files list
        with st.sidebar.container():
            # Display each file name
            for file in files:
                st.write(file)
    else:
        # If no files found, display a message
        st.sidebar.write("No files found in 'data' folder.")
    
    # File Uploader
    uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")
    
    # If file is uploaded
    if uploaded_file is not None:
        # Save PDF file to folder
        folder = "data"
        os.makedirs(folder, exist_ok=True)  # Create folder if it doesn't exist
        file_path = os.path.join(folder, uploaded_file.name)
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        # Show success message
        st.success(f"File '{uploaded_file.name}' saved!!")
        
        # Update list of files in the sidebar
        files = list_files()
        if files:
            # Create a container for the updated files list
            with st.sidebar.container():
                # Display each file name
                for file in files:
                    st.write(file)

    # User Input
    #user_input = st.text_input("Enter your query")

# Run the main function when the script is executed
if __name__ == "__main__":
    main()
