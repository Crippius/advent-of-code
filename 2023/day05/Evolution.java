package day05;

public enum Evolution {
    BAG,
    SEED,
    SOIL,
    FERTILIZER,
    WATER,
    LIGHT,
    TEMPERATURE,
    HUMIDITY,
    LOCATION;

    public Evolution nextState() {
        switch (this) {
            case BAG:
                return SEED;
            case SEED:
                return SOIL;
            case SOIL:
                return FERTILIZER;
            case FERTILIZER:
                return WATER;
            case WATER:
                return LIGHT;
            case LIGHT:
                return TEMPERATURE;
            case TEMPERATURE:
                return HUMIDITY;
            case HUMIDITY:
                return LOCATION;
            default:
                return SEED;
        }
    }
}
