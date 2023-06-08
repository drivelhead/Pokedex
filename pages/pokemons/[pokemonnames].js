import React from 'react'
import Image from 'next/image'
import {useRouter} from 'next/router'
// import Layout from '@/components/Layout'

export default function PokemonPage({details}) {
  const router = useRouter()
  return (
  // <Layout>
    <div> 
        <h1 className="p-4 bg-purple-300 text-300 text-center">Pokemon Page - {details.name} </h1>
        <div className="relative">
        <Image src ={details.imageURL} width={200} height={200}/> 
        </div>
        
        <div className="flex flex-col space-y-4 ">
           <p>Classification --{details.classification}</p>
           <p>Type 1 --{details.type1} </p>
          <p>Legendary --{details.is_legendary}</p>

          <div className="flex flex-col space-x-4 bg-cyan-200">
           <p>Height: {details.pokemonstats.height_m}</p>
           <p>Weight: {details.pokemonstats.weight_kg}</p>
           <p>Speed: {details.pokemonstats.speed}</p>
           <p>Attack: {details.pokemonstats.attack}</p>
           </div>
        </div>
    </div>
    // </Layout>
  )
}

export async function getServerSideProps(context){
  console.log("context", context.params)
  const pokemonName = context.params.pokemonnames
  const response = await fetch(`http://127.0.0.1:8000/pokemons/${pokemonName}`)
  let data = await response.json()  
  
const externalUrl = `https://pokeapi.co/api/v2/pokemon/${pokemonName.toLowerCase()}`

const externalDataResponse = await fetch(externalUrl)
const externalData = await externalDataResponse.json()

const imageURL = externalData.sprites.other.dream_world.front_default
  
console.log("data of single pokemon", imageURL)
 
data = { ...data, imageURL}
  return {
    props: {
      details: data
    }
  }
}