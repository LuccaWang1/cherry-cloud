import "./App.css";
import Background from "./flappy_cherry_components/background";

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <p>Welcome to CHERRY CLOUD!</p>

        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Let's code!
        </a>
        <h6>Flappy cherry green background</h6>
        <Background width={800} height={500} />

        <img src="cherry.webp" className="App-logo" alt="logo" />
      </header>
    </div>
  );
}

export default App;
