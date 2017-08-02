people = ['Dr. Veronica Bueno','Dr. Kevin Burgio','Colin Carlson','Giovanni Castaldo','Dr. Carrie Cizauskas','Dr. Christopher Clements','Dr. Graeme Cumming','Dr. Tad Dallas','Dr. Jorge Doña','Eric Dougherty','Sarah Fourby','Dr. Wayne Getz','Dr. Nyeema Harris','Dr. Roger Jovani','Zhongqi MIao','Dr. Sergei Mironov','Oliver Muellerklein','Dr. Anna J. Phillips','Dr. Heather Proctor','Hyun Seok Yoon']
ppl_img_url = []
text = '<h2> PEARL Team </h2>' + 
'<div class="team-cat">'
k=0
		for(i=0;i<Math.floor(people.length/3);i++){
			text += '<div class="row">'+
					for(j=0; j<3;j++){
					text += '<div calss="col-md-4" style="margin:auto;">'+
						'<img src="img/spiderman.jpg" class="img-circle" alt="Cinque Terre">'+
						'<h3 class="team-member">'+ people[k] +'</h3>'+
					'</div>';
					k+=1;
					}
			text += '</div>';
		}
		/*text+= '<div class="