class TodoItem extends React.Component {
    constructor(props) {

        super(props);
        console.log("TodoItem")
    }
    render() {

        return (
            <tr>  
                <td> {this.props.item.id}</td>
                <td> {this.props.item.name}</td>
                <td> <input type="checkbox" disabled="disabled" checked={this.props.item.isComplete} /> </td>

            </tr>
        )

    }

}

class Todo extends React.Component {
    constructor(props) {

        super(props);
        this.state = {
            data1: [],
        };

    }

    componentDidMount() { 

        fetch('https://localhost:44385/api/todo')
            .then(response => response.json())
            .then(data => { 
                this.setState({ data1: data });
            });
    }

    render() {

        const todoList = this.state.data1;
        console.log(todoList, "todoList", todoList.length);
        console.log("render",   todoList.length);
        return (
            <table className="table">
                <thead>
                    <tr>
                        <td>ID</td>
                        <td>Name</td>
                        <td>Completed</td>

                    </tr>
                </thead>
                <tbody>
                {
 
                    todoList.map(todo =>
                        <TodoItem key={todo.id} item={todo} />
                     )
                    }
                </tbody>
            </table>
        );
    }
}


 
ReactDOM.render(
    <Todo  />,
    document.getElementById('root')
);


 