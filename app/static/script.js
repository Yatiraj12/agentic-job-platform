async function searchJobs(){

const query=document.getElementById("jobQuery").value

if(!query){
alert("Enter a job search query")
return
}

document.getElementById("loading").classList.remove("hidden")
document.getElementById("results").classList.add("hidden")

const response=await fetch("/api/search-jobs",{

method:"POST",
headers:{
"Content-Type":"application/json"
},

body:JSON.stringify({
query:query
})

})

const data=await response.json()

document.getElementById("loading").classList.add("hidden")
document.getElementById("results").classList.remove("hidden")

let analysis=data.data.agent_output.analysis

// If response is string convert to JSON
if(typeof analysis==="string"){

try{
analysis=JSON.parse(analysis)
}catch(e){
analysis={raw_output:analysis}
}

}

document.getElementById("intent").textContent=analysis.user_intent || "No intent detected"
document.getElementById("skills").textContent=analysis.skills_detected || "No skills detected"

const queriesList=document.getElementById("queries")
queriesList.innerHTML=""

if(analysis.recommended_queries){

analysis.recommended_queries.forEach(q=>{
const li=document.createElement("li")
li.textContent=q
queriesList.appendChild(li)
})

}

const platformList=document.getElementById("platforms")
platformList.innerHTML=""

if(analysis.best_platforms){

analysis.best_platforms.forEach(p=>{
const li=document.createElement("li")
li.textContent=p
platformList.appendChild(li)
})

}

}