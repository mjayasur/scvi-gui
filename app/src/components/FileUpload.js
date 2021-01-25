import React from 'react';

class FileUpload extends React.Component {
  constructor() {
    super();
    this.state = {
      someKey: 'someValue'
    };
  }

  render() {
    return (
        <div className = "container">
            <div class="data-upload">
                <input type="file" class="custom-file-input" id="data-input" />
                <label class="custom-file-label" for="data-input">Upload data file with <code>.h5ad</code> extension</label>
            </div>
        </div>
    );
  }

  componentDidMount() {
    this.setState({
      someKey: 'otherValue'
    });
  }
}

export default FileUpload;
