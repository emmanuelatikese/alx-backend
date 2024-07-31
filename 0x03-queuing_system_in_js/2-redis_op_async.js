import { createClient, print } from 'redis';
import util from 'util';

const client = createClient();

client.on('connect', () =>{
    console.log('Redis client connected to the server');
}).on('error', (error) => {
    console.log(`Redis client not connected to the server: ${error}`);
})



const setNewSchool = (schoolName, value) =>{
    client.set(schoolName, value, print);
}
const getClient = util.promisify(client.get).bind(client);
const displaySchoolValue = async(schoolName) => {
    try{
        const ans = await getClient(schoolName);
        console.log(ans);
    }
    catch(error){
        console.error(error);
    }
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');