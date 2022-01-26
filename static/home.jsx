function CoinButton() {
    function alertMessage() {
      alert('You just handled an event!');
    }
  
    return (
      <button type="button" onClick={alertMessage}>
        Click me
      </button>
    );
  }


function RedButton(props) {
    return (
      <div>
        <button type="button" style={{backgroundColor: 'black', color: 'white'}}>
          {props.message}
        </button>
      </div>
    );
  }
  
  ReactDOM.render(
    (
      <div>
        <CoinButton message="Click me" />
      </div>
    ),
    document.querySelector('#root')
  );