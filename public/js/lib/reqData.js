function getTableObject(data){
    if(!Array.isArray(data) || data.lenth == 0) return undefined;
    
    table={};
    table.columns = Object.keys(data[0]);
    table.datas = data;

    return table;
}

function to_Table(data){
    tableData = getTableObject(data);
    console.log(tableData.columns);
    //make a table
    tableTag = document.createElement('table');
    tableTag.setAttribute('id', 'dataTable'); 
    tableTag.setAttribute('class', 'table table-bordered display nowrap dataTable dtr-inline collapsed') //bootstrap

    //헤드 태그
    theadTag = document.createElement('thead');
    tableTag.appendChild(theadTag);

    //컬럼 작업
    theadTrTag = document.createElement('tr');
    theadTag.appendChild(theadTrTag);

    for(var colName of tableData.columns){
        th = document.createElement('th');
        th.innerText = colName;
        theadTrTag.appendChild(th);
    }
    //바디 태그
    tbodyTag = document.createElement('tbody');
    tableTag.appendChild(tbodyTag);

    //행 작업
    for(var row of tableData.datas){
        tr = document.createElement('tr');
        
        for(var colName of tableData.columns){
            td = document.createElement('td');
            
            td.innerText = row[colName];
            
            if(colName === '종목코드'){
                td.setAttribute('class', 'request_column');
            }
            tr.appendChild(td);
        }
        tbodyTag.appendChild(tr);
    }
    
    return tableTag
}

function to_Chart(originData){
    labels = [];
    datas = [];

    for(var array of originData){
        datas.push(array['trClsPrc']);
        labels.push(array['trDt']);
    }

    canvas = document.createElement('canvas');

    chart = new Chart(canvas, {
        type: 'line',
        data: {
            labels: labels.reverse(),
            datasets: [{
            data: datas.reverse(),
            backgroundColor: ['#4e73df', '#1cc88a', '#36b9cc'],
            hoverBackgroundColor: ['#2e59d9', '#17a673', '#2c9faf'],
            hoverBorderColor: "rgba(234, 236, 244, 1)",
            }],
        },
     
    });

    return canvas;
}