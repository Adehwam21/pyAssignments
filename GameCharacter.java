public class GameCharacter{
    public String name;
    public int hitPoints;
    public int damagePoints;

    public GameCharacter(String name, int hitPoints, int damagePoints){
        this.name = name;
        this.hitPoints = hitPoints;
        this.damagePoints = damagePoints;
    }

    public String getName(){
        return name;
    }

    public void setName(String name){
        this.name = name;
    }

    public int getHitPoints(){
        return hitPoints;
    }

    public int getDamagePoints(){
        return damagePoints;
    }

    public void setHitPoints(int hitPoints){
        this.hitPoints = hitPoints;
    }

    public void setDamagePoints(int damagePoints){
        this.damagePoints = damagePoints;
    }

    public void attack(GameCharacter character){
        character.setHitPoints(character.getHitPoints() - 10);
    }
}

class Player extends GameCharacter{
    private int level;
    private int experiencePoints;

    public Player(String name, int hitPoints, int damagePoints, int level, int experiencePoints){
        super(name, hitPoints, damagePoints);
        this.level = level;
        this.experiencePoints = experiencePoints;
    }

    public int getLevel(){
        return level;
    }

    public int getExperiencePoints(){
        return experiencePoints;
    }

    public void setLevel(int level){
        this.level = level;
    }

    public void setExperiencePoints(int experiencePoints){
        this.experiencePoints = experiencePoints;
    }

    public void gainExperience(int experience){
        experiencePoints += experience;
        if(experiencePoints >= 100){
            level++;
            experiencePoints = 0;
            hitPoints += 10;
            damagePoints += 10;
        }
    }
}


class Enemy extends GameCharacter{
    private String type;

    public Enemy(String name, int hitPoints, int damagePoints, String type){
        super(name, hitPoints, damagePoints);
        this.type = type;
    }

    public String getType(){
        return type;
    }

    public void setType(String type){
        this.type = type;
    }

    public void attack(GameCharacter character){
        character.setHitPoints(character.getHitPoints() - 10);
        System.out.println("The enemy dealt " + 10 + " damage to " + character.getName());
    }
}

class Main{
    public static void main(String[] args){
        Player player = new Player("Player", 100, 10, 1, 0);
        Enemy enemy = new Enemy("Enemy", 100, 10, "Goblin");

        while(player.getHitPoints() > 0 && enemy.getHitPoints() > 0){
            player.attack(enemy);
            enemy.attack(player);
        }

        if(player.getHitPoints() <= 0){
            System.out.println("The player has died");
        }else{
            System.out.println("The enemy has died");
        }
    }
}