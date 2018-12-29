import { createAction, handleActions } from "redux-actions";

const SETDATA = "SETDATA";
const HANDLEPRICE = "HANDLEPRICE";
const SETPRICE = "SETPRICE"

export const setData = createAction(SETDATA);
export const handlePrice = createAction(HANDLEPRICE);
export const setPrice = createAction(SETPRICE);

const initialState = {
  id: "",
  datas: [],
  budget: -1,
  currentPrice: 0
};

export default handleActions(
  {
    [SETDATA]: (state, action) => {
      const { data, budget } = action.payload;
      return {
        ...state,
        datas: data.filtered,
        budget: Number(budget),
        id: data.id
      };
    },
    [HANDLEPRICE]: (state, action) => {
      return { ...state, currentPrice: state.currentPrice + action.payload };
    },
    [SETPRICE] : (state,action) => {
        return {...state, currentPrice : action.payload}
    }
  },
  initialState
);
