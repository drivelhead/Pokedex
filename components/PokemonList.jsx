import React from 'react'
import Link from "next/link"


const colorMap = {
    fire: 'bg-red-500',
    water:'bg-blue-500',
    grass: 'bg-green-500',
    bug: 'bg-purple-500',
    normal: 'bg-gray-500',
    poison: 'bg-orange-500',
    fighting: 'bg-yellow-500',
    ground: 'bg-black-400',
    electric: 'bg-cyan-500',
    ice: 'bg-pink-500',
    rock: 'bg-brown-200'
        
}

function PokemonListItem({pokemon}){

   
    return (
      <Link href={`/pokemons/${pokemon.name}`}>
         <li className="border border-gray-400 p-5 flex items-center space-x-4">
            <span className="flex items-center space-x-4">
            <div className={`w-20 h-20 text-green-50 rounded-full grid place-items-center font-semibold ${colorMap[pokemon.type1]}`}><span>
            {pokemon.type1}   
             </span>
             </div>
            <span className="text-gray-700 text-xl font-bold">{pokemon.name}</span>
            </span>
            <span className="text-gray-600 text-xl font-semibold">{pokemon.classfication}</span>
        </li>
        </Link>
    )
}

export default function PokemonList({pokemons}) {
  return (
    <ul>
{
    pokemons.length > 0 ? 
    pokemons.map((pokemon, index)=> <PokemonListItem pokemon={pokemon} key={index} />)
    : <h1 className="text-3xl text-gray-600"> No pokemons in database </h1>
}
    </ul>
  )
}
