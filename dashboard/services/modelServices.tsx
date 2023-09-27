import axios from 'axios';

const getAllModels: any = async () => {
    try {
        const response = await axios.get('http://localhost:8000/admin/models');
        if (response.status === 200) {
            console.log(response.data);
            return response.data;
        }
    } catch (error) {
        console.error(error);
    }
}

export { getAllModels };
