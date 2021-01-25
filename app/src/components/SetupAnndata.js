import React from 'react';

class SetupAnndata extends React.Component {
  constructor() {
    super();
    this.state = {
      someKey: 'someValue'
    };
  }

  render() {
    return (
        <div>
            <div class="setup-anndata">
                <div class="form-row">
                    <div class="form-group col-md-4">
                        <label class="setup-anndata">Batch Key</label>
                        <select class="form-control" id="batch-key-select">
                            <option>1</option>
                            <option>2</option>
                            <option>3</option>
                        </select>
                    </div>
                    <div class="form-group col-md-4">
                        <label class="setup-anndata">Labels Key</label>
                        <select class="form-control" id="labels-key-select">
                            <option>1</option>
                            <option>2</option>
                            <option>3</option>
                        </select>
                    </div>
                    <div class="form-group col-md-4">
                        <label class="setup-anndata">Layer</label>
                        <select class="form-control" id="layer-select">
                            <option>1</option>
                            <option>2</option>
                            <option>3</option>
                        </select>
                    </div>
                </div>
                <label class="setup-anndata">Protein Expression OBSM Key</label>
                <select class="form-control" id="obsm-key-select">
                    <option>1</option>
                    <option>2</option>
                    <option>3</option>
                </select>
                <label class="setup-anndata">Protein Names UNS Key</label>
                <select class="form-control" id="uns-key-select">
                    <option>1</option>
                    <option>2</option>
                    <option>3</option>
                </select>
                <label class="setup-anndata">Categorical Covariate Keys</label>
                <select multiple class="form-control" id="categorical-covariate-keys-select">
                    <option>1</option>
                    <option>2</option>
                    <option>3</option>
                </select>
                <label class="setup-anndata">Continuous Covariate Keys</label>
                <select multiple class="form-control" id="continuous-covariate-keys-select">
                    <option>1</option>
                    <option>2</option>
                    <option>3</option>
                </select>
                <input class="form-check-input" type="checkbox" value="" id="copy-of-anndata"></input>
                <label class="setup-anndata">Return a copy of adata?</label>
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

export default SetupAnndata;