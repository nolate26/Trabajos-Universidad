import './App.css'

function App() {
  return (
    <div className="App">
      <div>
        <img src="/assets/img/risk_logo.jpeg" className="logo react" alt="React logo" />
      </div>
      <h2>
        ¿Tienes lo necesario para dominar a tus carreras enemigas y conquistar San Joaquín en este juego de estrategia?
      </h2>
      <div>
        <img src='/assets/img/risk_portrait.jpeg' className='risk_portrait' alt="Risk San Joaquin" />
      </div>
      <a href='/sobre-nosotros'>Sobre nosotros</a>
      <a href='/pagina-principal'>Página principal</a>



      <div className='login-container'>
      </div>
      {/* <a href='/board'>Ir a Tablero</a> */}
    </div>
  )
}

export default App
