import React, {useEffect, useState} from 'react';
import api from '../../services/api'
import { trackPromise } from 'react-promise-tracker' 
import './style.css'
import LoadingIndicator from '../../componentes/LoadingIndicator'

export default function Dashboard(){
    
    const [filmes, setFilmes] = useState([])
    const [recomendacao, setRecomendacao] = useState([])
    useEffect(() => { 
        async function loadSpots(){
            const user_id = localStorage.getItem('user'); 
            const filmesAssistidos = await api.get('/users/'+user_id);
            const filmesRecomendados = await api.get('/recomendacao/'+user_id);
            console.log(filmesAssistidos.data)
            setRecomendacao(filmesRecomendados.data);
            setFilmes(filmesAssistidos.data);
        }
        trackPromise(
            loadSpots()
        );
    }, []);
    return (
        <>
            <div className="title">
                <strong>Filmes Assistidos</strong>
            </div>
                <LoadingIndicator/>
            <ul className="spot-list">
                {filmes.map( filme => (
                    <li key={filmes.movieId}>
                        <header className="header" style= {{ backgroundImage: `url(${filme.posterPath})`} }/>
                        <strong>{filme.title}</strong>
                        <span className="avaliacao"> Avaliação: {filme.avaliacao}</span>
                        <span>{filme.genres}</span>
                    </li>
                ))}
            </ul>
            <div></div>
            <div className="title">
                <strong>Filmes Recomendados</strong>
            </div>
            <LoadingIndicator/>
            <ul className="spot-list">
                {recomendacao.map( filme => (
                    <li key={filmes.movieId}>
                        <header style= {{ backgroundImage: `url(${filme.posterPath})` }}/>
                        <strong>{filme.title}</strong>
                        <span>{filme.genres}</span>
                    </li>
                ))}
            </ul>
        </>
    )
}
