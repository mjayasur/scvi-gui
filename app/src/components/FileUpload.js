import React from 'react';

class FileUpload extends React.Component {
  constructor() {
    super();
    this.state = {
      selectedFile: null
    };
  }


  onDataChange = event => {
    this.setState({ selectedFile: event.target.files[0] }); 
  }

  uploadData = () => {
    // Create an object of formData 
    const formData = new FormData(); 
    
    // Update the formData object 
    formData.append( 
      "anndata", 
      this.state.selectedFile, 
      this.state.selectedFile.name 
    ); 
    
    // Details of the uploaded file 
    console.log(this.state.selectedFile); 
    
    // Request made to the backend api 
    // Send formData object 
    // fill with flask shit


    // url = ""
    // axios.post(url, formData); 
  }

  render() {
    return (
      <div>
          
        <div className="row mt-3">
            <div className="col-5">
            <input onChange={this.onDataChange}  type="file" class="custom-file-input" id="data-input"  />

            <label className="custom-file-label" for="data-input">Upload data file with <code>.h5ad</code> extension</label>
            </div>

        </div>
                    <div className="row mt-2">
                    <button onClick={this.uploadData} type="button mt-4 " className="btn btn-success text-left">Upload</button>
        
                    </div>
                    </div>



    );
  }

  componentDidMount() {
    this.setState({
      
    });
  }
}

export default FileUpload;
