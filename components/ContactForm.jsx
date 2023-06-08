import {useState} from 'react'

function FormGroup({label, type, placeholder, value, onInput}){
    return( 
    <div className="flex flex-col space-y-2">
    <label>{label}</label>
    <input onInput={onInput} type={type} placeholder={placeholder} value={value} className="border border-gray-600 text-gray-800 rounded p-2 outline-none" />
        </div>)
}



export default function ContactForm() {
    const [fullname, setFullName] = useState("")
    const [email, setEmail] = useState("")
    const [message, setMessage] = useState("")

    function handleSubmit(e) {
        e.preventDefault()
        console.log("fullname", fullname)
        console.log("email", email)
        console.log("message", message)
    }

  return (
    <form onSubmit={handleSubmit} className="w-3/4 mx-auto flex flex-col space-y-3">
    
<FormGroup onInput={(e)=>setFullName(e.target.value)}    label="Name" type="text" placeholder="Your name" value={fullname} />

<FormGroup onInput={(e)=>setEmail(e.target.value)} value={email} label="Email" type="email" placeholder="Your email" />

<FormGroup onInput={(e)=>setMessage(e.target.value)} value={message} label="Message" type="text" placeholder="Your Message" />

<div className="text-center"> 
<button className="bg-purple-500 text-gray-50 px-6 py-2 rounded"> Send Message 
</button>
</div>
    </form>
  )
}
