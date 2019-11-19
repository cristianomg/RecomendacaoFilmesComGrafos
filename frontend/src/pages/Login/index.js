import React, {useState}  from 'react';
import api from '../../services/api';
import './style.css'

export default function Login( { history } ){
    
    const [userId, setUserId] = useState('');
    async function handleSubmit (event){  
      event.preventDefault();
      const response = await api.get('/user/'+userId)
      console.log(response)
      localStorage.setItem('user',userId);
      console.log(response.data)
      if (response.data === true ){
          history.push('/dashboard')
      }

    }
    return (
        <div className="container2">

            <form onSubmit={handleSubmit}>
                <label htmlFor= "email">Usuário *</label>
                <input 
                    type= "user"
                    id= "user" 
                    placeholder= "User Id"
                    value = {userId}
                    onChange = {event => setUserId(event.target.value)}
                />
            <button className= "btn" type= "submit" >Entrar</button>
        </form>
        </div>
    )
}