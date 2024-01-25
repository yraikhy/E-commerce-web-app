#!/usr/bin/env python3
from app import create_app, db
from app.models import Item

item1 = Item(name='Microwave', description='Warm/Cook your food easily! 5 Cooking Power Levels: There are five cooking power levels on this 700w microwave, allowing you to cook popcorn, potatoes, frozen vegetables, hot beverages, and more', picture='item1.jpeg', price=70, environmental_impact=80.9)
item2 = Item(name='Top Range Gaming PC + Montior/Accessories', description='System: Intel Core i9-11900KF Processor (8 Cores, 16 Threads, 3.50GHz Base, 5.30GHz Turbo, 16MB Cache) | Intel Z590 Chipset Motherboard | 32GB 2400MHz DDR4 RAM | 1TB M.2 NVMe SSD, GeForce RTX 3060', picture='item2.jpeg', price=2050, environmental_impact=71.5)
item3 = Item(name='Plant', description='Decorate your house with nature today!', picture='item3.jpeg', price=30, environmental_impact=1.9)
item4 = Item(name='Office Chair', description='Comfortable so you can get your work done!', picture='item4.jpeg', price=30, environmental_impact=14.5)

if __name__ == '__main__':
    app = create_app('development')
    with app.app_context():
        db.drop_all()
        db.create_all()
        db.session.add(item1)
        db.session.add(item2)
        db.session.add(item3)
        db.session.add(item4)
        db.session.commit()
    app.run(debug=True)