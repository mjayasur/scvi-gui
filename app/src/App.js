
import FileUpload from './components/FileUpload';
import './App.css';
import SetupAnndata from './components/SetupAnndata';
/*
1) upload anndata 
2) check boxes, dropdowns to run scvi.data.setup_anndata, like so they can in a graphical way change the arguments to the function
*/
function App() {
  return (
    <div className="App">
      <div className = "container">
        <FileUpload />
        <SetupAnndata />
      </div>
    </div>
  );
}

export default App;
